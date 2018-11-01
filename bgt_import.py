# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BGTImport
                                 A QGIS plugin
 Import Basisregistratie Grootschalige Topografie (BGT)
                              -------------------
        begin                : 2018-10-01
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Marco Duiker - MD-kwadraat
        email                : md@md-kwadraat.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import
from builtins import str
from builtins import object

from qgis.PyQt.Qt import Qt
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication,\
    QUrl
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QProgressBar, QApplication
from qgis.PyQt.QtGui import QIcon, QDesktopServices
from qgis.core import Qgis, QgsTask, QgsNetworkContentFetcherTask, QgsTaskManager,\
    QgsMessageLog, QgsProject, QgsApplication, QgsVectorLayer, QgsLayerDefinition,\
    QgsLayerTreeLayer, QgsMapLayerProxyModel
import processing

# Initialize Qt resources from file resources.py
from . import resources
# Import the code for the dialog
from .bgt_import_dialog import BGTImportDialog

try:
    import lxml.etree as le
except:
    from xml import etree

from functools import partial
import glob
import ogr
import os
import shutil
import tempfile
import time
import uuid
import webbrowser
from xml.dom.pulldom import parse

from .network import networkaccessmanager
from .bgt_utils import utils as bgt_utils


__author__ = 'Marco Duiker MD-kwadraat'
__date__ = 'October 2018'


_can_symlink = None
def can_symlink(folder):
    global _can_symlink
    if _can_symlink is not None:
        return _can_symlink
    symlink_path = os.path.join(folder, "can_symlink")
    try:
        os.symlink(folder, symlink_path)
        can = True
    except (OSError, NotImplementedError, AttributeError):
        can = False
    else:
        os.remove(symlink_path)
    _can_symlink = can
    return can


class BGTImport(object):
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'BGTImport_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&BGT Import')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'BGTImport')
        self.toolbar.setObjectName(u'BGTImport')
        
        self.nam = networkaccessmanager.NetworkAccessManager()
        self.project = QgsProject.instance()

    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """

        return QCoreApplication.translate('BGTImport', message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = BGTImportDialog()

        # define some connections
        self.dlg.fileBrowseButton_2.clicked.connect(self.chooseFile)
        self.dlg.help_btn.clicked.connect(self.showHelp)
        
        # modify some widgets
        self.dlg.save_gpkg_cmb.setStorageMode(3)        # gives us a save button
        self.dlg.download_layer_cmb.setFilters(QgsMapLayerProxyModel.VectorLayer)

        # add the buttons to the interface
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/BGTImport/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'BGT Import'),
            callback=self.run,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        for action in self.actions:
            self.iface.removePluginVectorMenu(
                self.tr(u'&BGT Import'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def getGeometryTypes(self, gml_file, requested_geometry_types, max_num_objects = False):
        '''determines geometry types and names in a bgt-file'''

        num_objects = 0
        num_requested_geom_types = len(requested_geometry_types)
        geom_types = []
        geom_names = {}
        geom_paths = {}

        try:
            doc = parse(gml_file)
        except Exception as v:
            QgsMessageLog.logMessage(u'Error parsing gml: ' + str(v), 'BGTImport')
            return geom_names, geom_paths

        in_geometry = False
        ogr_el_path = []
        try:
            for event,node in doc:
                if node.nodeName == 'imgeo:identificatie':
                    ogr_el_path = []
                    num_objects = num_objects + 0.5                         # this code is hit twice for each object
                    if max_num_objects and num_objects > max_num_objects:
                        break
                elif event.title() == 'Start_Element':
                    ogr_el_path.append(node.localName)
                elif event.title() == 'End_Element'  and len(ogr_el_path) > 0:
                    ogr_el_path.pop()
                if 'imgeo:geometrie' in node.nodeName or 'imgeo:positie' in node.nodeName:
                    geom_name = node.localName
                    in_geometry = True
                if 'gml:' in node.nodeName and in_geometry:
                    node_name = str(node.nodeName).lower()
                    in_geometry = False
                    if ((not 'Polygon' in geom_types) and 'Polygon' in requested_geometry_types) \
                    and ('polygon' in node_name or 'surface' in node_name):
                        geom_types.append('Polygon')
                        geom_names['Polygon'] = geom_name 
                        geom_paths['Polygon'] = ogr_el_path[:-1]
                    elif ((not 'LineString' in geom_types) and 'LineString' in requested_geometry_types) \
                    and 'linestring' in node_name:
                        geom_types.append('LineString')
                        geom_names['LineString'] = geom_name
                        geom_paths['LineString'] = ogr_el_path[:-1]
                    elif ((not 'Point' in geom_types) and 'Point' in requested_geometry_types) \
                    and 'point' in node_name:
                        geom_types.append('Point')
                        geom_names['Point'] = geom_name
                        geom_paths['Point'] = ogr_el_path[:-1]
                if len(geom_types) == num_requested_geom_types:
                    self.results[gml_file] = {'geom_names': geom_names, 'geom_paths': geom_paths}
                    return geom_names, geom_paths
        except Exception as v:
            QgsMessageLog.logMessage(u'Error parsing gml: ' + str(v), 'BGTImport')

        self.results[gml_file] = {'geom_names': geom_names, 'geom_paths': geom_paths}
        return geom_names, geom_paths


    def chooseFile(self):
        """Reacts on browse button and opens the right file selector dialog"""

        fileNames = QFileDialog.getOpenFileNames(caption = self.tr(u"Select BGT gml file(s)"), 
                                                 directory = '', 
                                                 filter = '*.gml')
        self.fileNames = ';'.join(fileNames[0])
        self.dlg.fileNameBox.setText(self.fileNames)

    def showHelp(self):
        """Reacts on help button"""

        #qgis.utils.showPluginHelp(filename = 'help/index')
        QDesktopServices().openUrl(QUrl.fromLocalFile( \
            os.path.join("file://", self.plugin_dir, 'help/build/html', \
                         'index.html')))


    def tiles_to_download(self):
        """Finds the tiles to download from BGT"""

        # Gets the tile numbers by intersecting with the grid
        tiles_to_request = []
        
        if self.dlg.download_layer_rbt.isChecked():
            # select tiles intersecting a layer
            select_layer = self.dlg.download_layer_cmb.currentLayer()
            if select_layer.selectedFeatureCount() \
            and self.dlg.selected_features_cbx.isChecked():
                # selected features only
                result = processing.run("native:saveselectedfeatures", 
                                        {'INPUT': select_layer,
                                         'OUTPUT': 'memory:selectie'})
                select_layer = result['OUTPUT']
                
            result = processing.run("native:extractbylocation", 
                                    {'INPUT': os.path.join(self.plugin_dir, \
                                              'bgt_grid.gpkg'),
                                     'PREDICATE': 0,
                                     'INTERSECT': select_layer,
                                     'OUTPUT': 'memory:tiles'})
                                     
            for feature in result['OUTPUT'].getFeatures():
                tiles_to_request.append(feature["tile"])
            if select_layer.selectedFeatureCount() \
            and self.dlg.selected_features_cbx.isChecked():
                QgsProject.instance().removeMapLayer(select_layer.id())
            QgsProject.instance().removeMapLayer(result['OUTPUT'].id())
            
        if self.dlg.download_map_extent_rbt.isChecked():
            # select tiles intersecting the map extent
            wkt_extent = self.iface.mapCanvas().extent().asWktPolygon()

            driver = ogr.GetDriverByName("GPKG")
            dataSource = driver.Open(os.path.join(self.plugin_dir, 'bgt_grid.gpkg'), 0)
            grid = dataSource.GetLayer()
            grid.SetSpatialFilter(ogr.CreateGeometryFromWkt(wkt_extent))

            for feature in grid:
                tiles_to_request.append(feature.GetField("tile"))
                
        return tiles_to_request

    def tiles_download_url(self, tiles):
        '''Returns the BGT download url for a set of tiles'''
        
        return "https://downloads.pdok.nl/service/extract.zip?" +\
        "extractname=bgt&extractset=citygml&excludedtypes=plaatsbepalingspunt&history=true&" +\
        "tiles=%7B%22layers%22%3A%5B%7B%22aggregateLevel%22%3A0%2C%22codes%22%3A%5B" + \
        '%2C'.join([str(x) for x in tiles]) + "%5D%7D%5D%7D"


    def add_layer_to_group(self, geopackage, layer, group):
        '''
        Adds a layer to the group and returns the layer
        '''
        
        uri = '%s|layername=%s|subset="eindRegistratie" IS NULL' % (geopackage, layer)
        map_layer = QgsVectorLayer(uri, 
            layer.replace('bgt_','').replace('_P',' (punt)').replace('_L',' (lijn)').replace('_V', ' (vlak)'), 
            "ogr")
        self.project.addMapLayer(map_layer, False)
        group.insertChildNode(-1, QgsLayerTreeLayer(map_layer))
        
        return map_layer
        
    def add_styling(self, map_layer, layer):
        '''
        Adds the styling to the layer. The user has the option to 
        overrule the style by placing something in the user_qml folder.
        '''
        
        qml_folder = os.path.join(self.plugin_dir,'qml')
        user_qml_folder = os.path.join(self.plugin_dir,'user_qml')
        
        qml = os.path.join(qml_folder,layer + '.qml')
        user_qml = os.path.join(user_qml_folder,layer + '.qml')
        if os.path.exists(user_qml):
            qml = user_qml
        if os.path.exists(qml):
            map_layer.loadNamedStyle(qml) 


    def add_to_project(self, task, geopackage):
        '''
        Adds layers applying filtering and styles on the go.
        When done, save the whole shebang to a qlr for easy access.
        '''
        
        progress = 0
        if task:
            task.setProgress(progress)
        
        import_folder = os.path.dirname(geopackage)
        
        # add a layergroup to insert the layers in
        layer_group = QgsProject.instance().layerTreeRoot().insertGroup(0, 
            os.path.basename(geopackage)[:-5])
        
        standard_layers = bgt_utils.get_standard_layers()
        layers_added = []
        layers = []
        gp =  ogr.GetDriverByName('GPKG').Open( geopackage )
        for i in range(gp.GetLayerCount()):
            layers.append(gp.GetLayerByIndex(i).GetName())
        increment = 100/len(layers)
        
        # first add all standard layers this plugin knows
        for layer in standard_layers:
            if layer in layers:
                map_layer = self.add_layer_to_group(geopackage, layer, layer_group)
                self.add_styling(map_layer, layer)
                # turn layers on and of
                if not layer in bgt_utils.get_visible_layers():
                    self.project.layerTreeRoot().findLayer(map_layer.id()).setItemVisibilityChecked(False)                  
                layers_added.append(layer)
                progress = progress + increment
                if task:
                    task.setProgress(progress)
                
        # then add all layers we might have missed
        # should not happen as we don't have .gfs for those ...
        missed_layers = list(set(layers) - set(layers_added))
        if missed_layers:
            progress = 0
            increment = 100/len(missed_layers)
            for layer in missed_layers:
                map_layer = self.add_layer_to_group(geopackage, layer, layer_group)
                if task:
                    task.setProgress(progress)
                    
        # now save the whole shebang in qlr file:
        # Unfortunately we cannot save the group itself. And if we save the chilren we miss the group header
        # So we leave this up to the user.
        #QgsLayerDefinition.exportLayerDefinition(geopackage.replace('.gpkg','.qlr'), 
        #   self.project.layerTreeRoot().findGroup(os.path.basename(geopackage)[:-5]).children())
        if task:
            task.setProgress(100)

    def download_task_failed(self, task_to_cancel):
        '''Show a message that the download has failed; cancel next task'''
        
        task_to_cancel.cancel()
        self.iface.messageBar().pushMessage("Error",
            self.tr(u'Downloading BGT tiles failed.') + u' ' +
            self.tr(u'See message log for more info.'), level = Qgis.Critical)

    def import_task_failed(self, task_to_cancel):
        '''Show a message that the import has failed; cancel next task'''
        
        self.iface.messageBar().pushMessage("Error",
            self.tr(u'Importing BGT tiles failed.') + u' ' +
            self.tr(u'See message log for more info.'), level = Qgis.Critical)
            
    def add_to_project_task_failed(self):
        '''Show a message that adding to project has failed'''
        
        self.iface.messageBar().pushMessage("Error",
            self.tr(u'Adding BGT tiles to project failed.') + u' ' +
            self.tr(u'See message log for more info.'), level = Qgis.Critical)

    def import_finished(self):
        """
        Inform the user everything is done
        """

        self.iface.messageBar().pushMessage("Info",
                self.tr(u'Done importing BGT data.'))


    def run(self):
        """Import and optionally add chosen files"""
        
        self.dlg.show()
        result = self.dlg.exec_()
        
        ########### TAB 0: new style processing of complete zip ################
        
        if result and self.dlg.tabWidget.currentIndex() == 0:
            QApplication.setOverrideCursor(Qt.WaitCursor)
            download_task = None
            if self.dlg.download_map_extent_rbt.isChecked() \
            or self.dlg.download_layer_rbt.isChecked():
                tiles = self.tiles_to_download()
                zip_file_name = os.path.join(tempfile.gettempdir(), 'extract-' + str(uuid.uuid4()) +'.zip')
                #download_task = QgsNetworkContentFetcherTask(QUrl(self.tiles_download_url(tiles)))
                # the QgsNetworkContentFetcherTask doesn't give a nice progress indication
                download_task = QgsTask.fromFunction(
                    'BGTImport: download tiles', 
                    bgt_utils.download_tiles, 
                    tiles = tiles, 
                    file_name = zip_file_name,
                    nam = self.nam)

            if self.dlg.import_existing_zip_rbt.isChecked():
                zip_file_name = self.dlg.open_zip_cmb.filePath()
                
            geopackage = self.dlg.save_gpkg_cmb.filePath()
            import_task = QgsTask.fromFunction(
                'BGTImport: (download and) import tiles', 
                bgt_utils.import_to_geopackage, 
                zip_file_name = zip_file_name,
                geopackage = geopackage)
                # , on_finished = self.import_finished(geopackage)
                # fires directly, instead of waiting for a task to finish?
            add_to_project_task = QgsTask.fromFunction(
                'BGTImport: (download and) import tiles', 
                self.add_to_project,
                geopackage = geopackage)
            QApplication.restoreOverrideCursor()
            if download_task:
                import_task.addSubTask(download_task,[],QgsTask.ParentDependsOnSubTask)
                self.iface.messageBar().pushMessage("Info",
                    self.tr(u'Started downloading and importing BGT tiles ...'))
                download_task.taskTerminated.connect(partial(self.download_task_failed, import_task))
            else:
                self.iface.messageBar().pushMessage("Info",
                    self.tr(u'Started importing BGT tiles ...'))
             
            self.tsk_mngr = QgsApplication.taskManager()   
            if self.dlg.add_cbx.isChecked():
                add_to_project_task.addSubTask(import_task,[],QgsTask.ParentDependsOnSubTask)
                add_to_project_task.taskCompleted.connect(self.import_finished)
                add_to_project_task.taskTerminated.connect(self.add_to_project_task_failed)
                self.tsk_mngr.addTask(add_to_project_task)
            else:
                import_task.taskCompleted.connect(self.import_finished)
                import_task.taskTerminated.connect(partial(self.import_task_failed, add_to_project_task))
                self.tsk_mngr.addTask(import_task)

            self.dlg.close()

        ########### TAB 1: old style processing of individual files ############
        # usefull if BGT definitions are changed.                              #
        # With this tab we can check if a fresh import looks the same as the   #
        # automatic one on tab 0.                                              #
        if result and self.dlg.tabWidget.currentIndex() == 1:
            # get all stuff from the dialog
            geometry_types = []
            if self.dlg.polygon_cbx.isChecked():
                geometry_types.append('Polygon')
            if self.dlg.line_cbx.isChecked():
                geometry_types.append('LineString')
            if self.dlg.point_cbx.isChecked():
                geometry_types.append('Point')

            max_num_objects = False
            if self.dlg.max_num_object_cbx.isChecked():
                max_num_objects = self.dlg.max_num_object_sbx.value()

            file_names_list = self.fileNames.split(';')
            number_of_files = len(file_names_list)

            # set up some user communication
            QApplication.setOverrideCursor(Qt.WaitCursor)

            self.iface.messageBar().pushMessage("Info",
                self.tr(u'Start') + ' ' + self.tr(u'Importing BGT gml files ...'))
            progressMessageBar = self.iface.messageBar().createMessage( \
                self.tr(u'Importing BGT gml files ...'))
            bar = QProgressBar()
            bar.setRange(0,0)
            bar.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(bar)
            self.iface.messageBar().pushWidget(progressMessageBar, Qgis.Info)

            # test symlinking
            self._can_symlink = _can_symlink = can_symlink(os.path.abspath(os.path.dirname(file_names_list[0])))

            # import the files
            count = 0
            self.results = {}
            for file_name in file_names_list:
                count = count + 1
                progressMessageBar.setText(self.tr(u"Analyzing file ") + str(count) + self.tr(u" from ") 
                    + str(number_of_files) + ": " + os.path.basename(file_name))
                # find the ogr paths to the requested geometries
                geom_names, geom_paths = self.getGeometryTypes(file_name, geometry_types, max_num_objects)

                if len(geom_paths) == 0:
                    self.iface.messageBar().pushMessage('Error', 
                        self.tr(u"Could not find any of the requested geometries in: " + 
                        os.path.basename(file_name)), level=Qgis.WARNING)
                else: 
                    for geom_type, geom_path in list(geom_paths.items()):
                        geom_name = geom_path[0]
                        progressMessageBar.setText( self.tr(u"Importing file ") + 
                            str(count) + self.tr(u" from ") + str(number_of_files) + 
                            ": " + os.path.basename(file_name))

                        #copy or symlink gml so we can add an appropriate gfs
                        if 'Polygon' in geom_type: 
                            gml_name = file_name[:-4] + '_V.gml'
                        elif 'LineString' in geom_type: 
                            gml_name = file_name[:-4] + '_L.gml'
                        elif 'Point' in geom_type: 
                            gml_name = file_name[:-4] + '_P.gml'

                        try:
                            if os.path.exists(gml_name):
                                os.remove(gml_name)
                            if _can_symlink:
                                os.symlink(os.path.basename(file_name), gml_name)
                            else:
                                shutil.copy(file_name,gml_name)
                        except Exception as v:
                            self.iface.messageBar().pushMessage('Error', 
                                self.tr(u"Error in creating gml copies for import: ") + 
                                str(v), level=Qgis.Warning)  
                            QgsMessageLog.logMessage(u'Error in creating gml copies for import: ' + 
                                str(v), 'BGTImport')
                        else:
                            gfs_name = gml_name[:-4] + '.gfs'
                            driver = ogr.GetDriverByName('gml')
                            try:
                                if os.path.exists(gml_name):
                                    if os.path.exists(gfs_name):
                                        os.remove(gfs_name)
                                    # create fresh gfs:
                                    gml = driver.Open(gml_name)
                                    # and add our own geometry definition to it:
                                    with open(gfs_name,'r') as f:
                                        gfs = f.read()
                            except Exception as v:
                                self.iface.messageBar().pushMessage('Error', 
                                    self.tr(u"Error in reading import definitions: ") + 
                                    str(v), level=Qgis.Warning)  
                                QgsMessageLog.logMessage(u'Error in reading import definitions: ' + str(v), 'BGTImport')
                            else:
                                gfs_fragment = "<GeomPropertyDefn><Name>%s</Name><ElementPath>%s</ElementPath><Type>%s</Type></GeomPropertyDefn>" % (geom_name,'|'.join(geom_path),geom_type)
                                gfs = gfs.replace('<GMLFeatureClass>','<GMLFeatureClass>' + gfs_fragment)
                                try:
                                    with open(gfs_name,'w') as f:
                                        f.write(gfs)
                                except Exception as v:
                                    self.iface.messageBar().pushMessage('Error', 
                                        self.tr(u"Error in writing import definitions: ") + 
                                        str(v), level=Qgis.Warning)  
                                    QgsMessageLog.logMessage(u'Error in writing import definitions: ' + str(v), 'BGTImport')
                                else:
                                    if self.dlg.add_cbx.isChecked():
                                        progressMessageBar.setText(self.tr(u"Adding file ") + str(count) + self.tr(u" from ") + 
                                               str(number_of_files) + ": " + os.path.basename(gml_name))
                                        self.iface.addVectorLayer(gml_name,os.path.basename(file_name)[:-4],'ogr')
                                        #    def add_styling(self, map_layer, layer):

            QApplication.restoreOverrideCursor()

            progressMessageBar.setText(self.tr(u"Importing BGT gml files done!"))
            bar.setRange(0,100)
            bar.setValue(100)

