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

import qgis

from qgis.PyQt import QtCore
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication,\
    QUrl, Qt
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QProgressBar, QApplication, \
    QMessageBox
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
from osgeo import ogr
import os
import shutil
import tempfile
import time
import uuid
import webbrowser
from xml.dom.pulldom import parse

from .bgt_utils import utils as bgt_utils

ogr.UseExceptions() 


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

        self.toolbar = self.iface.addToolBar(u'BGTImport')
        self.toolbar.setObjectName(u'BGTImport')
        
        self.project = QgsProject.instance()
        self.tsk_mngr = QgsApplication.taskManager()

        # Create the dialog (after translation) and keep reference
        self.dlg = BGTImportDialog()

        # define some connections
        self.dlg.download_map_extent_rbt.toggled.connect(self.radio_toggled)
        self.dlg.download_layer_rbt.toggled.connect(self.radio_toggled)
        #self.dlg.import_existing_zip_rbt.toggled.connect(self.radio_toggled)
        # disable the widgets associated to unselected radio buttons
        self.radio_toggled()
        
        self.dlg.download_btn.clicked.connect(self.download_zip)
        self.dlg.convert_btn.clicked.connect(self.convert_bgt_to_gpkg)
        self.dlg.add_btn.clicked.connect(self.add_to_project)
        self.dlg.import_btn.clicked.connect(self.import_individual_files)
        self.dlg.fileBrowseButton_2.clicked.connect(self.chooseFile)
            
        self.dlg.help_btn.clicked.connect(self.showHelp)
        self.dlg.close_btn.clicked.connect(self.close_bgt_dialog)
        
        # modify some widgets
        self.dlg.save_to_gpkg_cmb.setStorageMode(3) # gives us a save button
        self.dlg.save_zip_cmb.setStorageMode(3) 
        self.dlg.download_layer_cmb.setFilters(QgsMapLayerProxyModel.VectorLayer)
        
        for ft in bgt_utils.get_featuretypes():
            self.dlg.featuretypes_cbx.addItemWithCheckState(
                ft, Qt.CheckState.Checked)
        
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
        '''
        Determines geometry types and names in a bgt-file. 
        All geometry types are forced to the multi-type.
        '''

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
                    if ((not 'MultiPolygon' in geom_types) and 'Polygon' in requested_geometry_types) \
                    and ('polygon' in node_name or 'surface' in node_name):
                        geom_types.append('MultiPolygon')
                        geom_names['MultiPolygon'] = geom_name 
                        geom_paths['MultiPolygon'] = ogr_el_path[:-1]
                    elif ((not 'MultiLineString' in geom_types) and 'LineString' in requested_geometry_types) \
                    and 'linestring' in node_name:
                        geom_types.append('MultiLineString')
                        geom_names['MultiLineString'] = geom_name
                        geom_paths['MultiLineString'] = ogr_el_path[:-1]
                    elif ((not 'MultiPoint' in geom_types) and 'Point' in requested_geometry_types) \
                    and 'point' in node_name:
                        geom_types.append('MultiPoint')
                        geom_names['MultiPoint'] = geom_name
                        geom_paths['MultiPoint'] = ogr_el_path[:-1]
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

        QDesktopServices().openUrl(QUrl(
            "https://marcoduiker.github.io/QGIS_BGT_Import/help/build/html/index.html"))

    def radio_toggled(self):
        '''Toggles the widgets associated with a radio button'''
        
        self.dlg.selected_features_cbx.setEnabled(self.dlg.download_layer_rbt.isChecked())
        self.dlg.download_layer_cmb.setEnabled(self.dlg.download_layer_rbt.isChecked())

    def download_finished(self):
        """Shows a message download has finished."""
        self.iface.messageBar().pushMessage("Info",
                self.tr(u'Done downloading BGT zip.'))

        self.dlg.open_zip_cmb.setFilePath(
            self.dlg.save_zip_cmb.filePath())
            
        self.dlg.tabWidget.setCurrentIndex(1)
        
        
    def download_zip(self):
        """
        Download BGT zip file.
        """
        
        zip_file_name = self.dlg.save_zip_cmb.filePath()
        if os.path.exists(zip_file_name):
            if not os.access(zip_file_name, os.W_OK):
                self.iface.messageBar().pushMessage("Error",
                    self.tr(u'Selected file not writeable.'), level = Qgis.Critical)    
                return
            os.remove(zip_file_name)
        elif not os.access(os.path.dirname(zip_file_name), os.W_OK):
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'Selected folder not writeable.'), 
                level = Qgis.Critical)    
            return
        
        if self.dlg.download_layer_rbt.isChecked():
            # select BGT by intersecting with a layer
            select_layer = self.dlg.download_layer_cmb.currentLayer()
            if select_layer.selectedFeatureCount() \
            and self.dlg.selected_features_cbx.isChecked():
                # selected features only
                result = processing.run("native:saveselectedfeatures", 
                                        {'INPUT': select_layer,
                                         'OUTPUT': 'memory:selectie'})
                select_layer = result['OUTPUT']
            wkt_extent = select_layer.extent().asWktPolygon()
            
        if self.dlg.download_map_extent_rbt.isChecked():
            wkt_extent = self.iface.mapCanvas().extent().asWktPolygon()
        
        QgsMessageLog.logMessage( u'Download area: ' + wkt_extent, 
                                  tag = 'BGTImport', level = Qgis.Info)
                               
        download_task = QgsTask.fromFunction(
            'BGTImport: download zip', 
            bgt_utils.download_zip, 
            geofilter = wkt_extent, 
            featuretypes = self.dlg.featuretypes_cbx.checkedItems(),
            file_name = zip_file_name)

        download_task.taskCompleted.connect(self.download_finished)
        self.tsk_mngr.addTask(download_task)
        
        
    def convert_bgt_to_gpkg(self):
        """
        New style of processing with predefined definitions.
        """
        
        geopackage = self.dlg.save_to_gpkg_cmb.filePath()
        if os.path.exists(geopackage):
            if not os.access(geopackage, os.W_OK):
                self.iface.messageBar().pushMessage("Error",
                    self.tr(u'Selected file not writeable.'), 
                    level = Qgis.Critical)    
                return
            os.remove(geopackage)
        elif not os.access(os.path.dirname(geopackage), os.W_OK):
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'Selected folder not writeable.'), 
                level = Qgis.Critical)    
            return

        zip_file_name = self.dlg.open_zip_cmb.filePath()
        if not os.path.exists(zip_file_name):
            self.iface.messageBar().pushMessage("Error",
            self.tr(u'No zip file selected.'), level = Qgis.Critical)    
            return
            
        import_task = QgsTask.fromFunction(
            'BGTImport: convert .zip to .gpkg', 
            bgt_utils.import_to_geopackage, 
            zip_file_name = zip_file_name,
            geopackage = geopackage)
        
        self.iface.messageBar().pushMessage("Info",
            self.tr(u'Started converting ...'))
         
        import_task.taskCompleted.connect(self.import_finished)
        self.tsk_mngr.addTask(import_task)


    def import_individual_files(self):
        """
        old style processing of individual files
        usefull if BGT definitions are changed.                              
        With this tab we can check if a fresh import looks the same as the
        automatic one with predefined defintions.                                            
        """
        
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

        try:
            file_names_list = self.fileNames.split(';')
            number_of_files = len(file_names_list)
            if not number_of_files:
                raise Exception()
        except:
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'Select at least one file to import.'), level = Qgis.Critical)    
            return

        # set up some user communication
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.iface.messageBar().pushMessage("Info",
            self.tr(u'Start') + ' ' + self.tr(u'Importing BGT gml files ...'))
        progressMessageBar = self.iface.messageBar().createMessage( \
            self.tr(u'Importing BGT gml files ...'))
        bar = QProgressBar()
        bar.setRange(0,0)
        bar.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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
                    os.path.basename(file_name)), level=Qgis.Warning)
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
                            finally:
                                gml.Close()

        QApplication.restoreOverrideCursor()

        progressMessageBar.setText(self.tr(u"Importing BGT gml files done!"))
        bar.setRange(0,100)
        bar.setValue(100)


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


    def add_to_project(self, task = None, geopackage = None):
        '''
        Adds layers applying filtering and styles on the go.
        When done, save the whole shebang to a qlr for easy access.

        !!! THIS PROBABLY SHOULD BE DONE IN THE MAIN THREAD: https://stackoverflow.com/questions/14541477/qobjectconnect-cannot-queue-arguments-of-type-qvectorint

        '''
        
        progress = 0
        if task:
            task.setProgress(progress)
            
        if not geopackage:
            geopackage = self.dlg.open_gpkg_cmb.filePath()
            
        if not os.path.exists(os.path.dirname(geopackage)):
            self.iface.messageBar().pushMessage("Error",
                self.tr(u'No file selected to save the imports to.'), level = Qgis.Critical)    
            return
        
        import_folder = os.path.dirname(geopackage)
        
        # add a layergroup to insert the layers in
        QgsMessageLog.logMessage(u'Adding layer group to project ...', 
                                  'BGTImport', level=Qgis.Info)
        layer_group = QgsProject.instance().layerTreeRoot().insertGroup(0, 
            os.path.basename(geopackage)[:-5])
        
        standard_layers = bgt_utils.get_standard_layers()
        layers_added = []
        layers = []
        QgsMessageLog.logMessage(u'Opening geopackage ...' , 
                                  'BGTImport', level=Qgis.Info)
        gp =  ogr.GetDriverByName('GPKG').Open( geopackage )
        QgsMessageLog.logMessage(u'Getting a layer inventory ...',
                                      'BGTImport', level=Qgis.Info)
        for i in range(gp.GetLayerCount()):
            layers.append(gp.GetLayerByIndex(i).GetName())
            QgsMessageLog.logMessage(u'Found layer "' + layers[-1] + '"',
                                      'BGTImport', level=Qgis.Info)
        increment = 100/len(layers)
        
        # first add all standard layers this plugin knows
        QgsMessageLog.logMessage(u'Start adding layers ...',
                                  'BGTImport', level=Qgis.Info)
        for layer in standard_layers:
            if layer in layers:
                QgsMessageLog.logMessage(u'Adding layer "' + str(layer) + \
                                          '" to project.' , 'BGTImport',
                                          level=Qgis.Info)
                try:
                    map_layer = self.add_layer_to_group(geopackage, layer, layer_group)
                    self.add_styling(map_layer, layer)
                    layers_added.append(layer)
                    # turn layers on and of
                    if not layer in bgt_utils.get_visible_layers():
                        self.project.layerTreeRoot().findLayer(map_layer.id()).setItemVisibilityChecked(False)                  
                    progress = progress + increment
                    if task:
                        task.setProgress(progress)
                except Exception as v:
                    progress = progress + increment
                    if task:
                        task.setProgress(progress)
                    QgsMessageLog.logMessage(
                        u'Failed to add layer "' + str(layer) + \
                         '" with message: ' + str(v), 
                        'BGTImport',
                        level=Qgis.Warning)
                
        # then add all layers we might have missed
        # should not happen as we don't have .gfs for those ...
        missed_layers = list(set(layers) - set(layers_added))
        if missed_layers:
            QgsMessageLog.logMessage(u'Found some unexpected layers, adding those as well...',
                                      'BGTImport', level=Qgis.Warning)
            progress = 0
            increment = 100/len(missed_layers)
            for layer in missed_layers:
                map_layer = self.add_layer_to_group(geopackage, layer, layer_group)
                QgsMessageLog.logMessage(u'Adding layer "' + str(layer) + \
                                          '" to project.' , 'BGTImport',
                                          level=Qgis.Info)
                if task:
                    task.setProgress(progress)
        
        if self.dlg.qlr_cbx.isChecked():            
            # save the whole shebang in qlr file:
            QgsMessageLog.logMessage(u'Saving the group layer as a layer file ...' ,
                                      'BGTImport', level=Qgis.Info)
            QgsLayerDefinition.exportLayerDefinition(geopackage.replace('.gpkg','.qlr'),
                [QgsProject.instance().layerTreeRoot().findGroup(os.path.basename(geopackage)[:-5])])

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
        """Inform the user conversion is done"""

        self.iface.messageBar().pushMessage("Info",
                self.tr(u'Done importing BGT data.'))
                
        self.dlg.open_gpkg_cmb.setFilePath(
            self.dlg.save_to_gpkg_cmb.filePath())
            
        self.dlg.tabWidget.setCurrentIndex(2)

    def close_bgt_dialog(self):
        self.dlg.hide()

    def run(self):
        """
        Import and optionally add chosen files
        
        This is deprecated and replaced by actions on several tabs
        """
        
        self.dlg.show()

