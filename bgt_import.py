# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BGTImport
                                 A QGIS plugin
 Import Basisregistratie Grootschalige Topografie (BGT)
                              -------------------
        begin                : 2017-06-28
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Marco Duiker - MD-kwadraat
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
from PyQt4.QtCore import *
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import *
from PyQt4.QtGui import QAction, QIcon
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from bgt_import_dialog import BGTImportDialog

from xml.dom.pulldom import parse
import ogr
import os
import shutil
import time
import webbrowser

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


class BGTImport:
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

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
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

        QObject.connect(self.dlg.fileBrowseButton_2, SIGNAL("clicked()"), self.chooseFile)
        QObject.connect(self.dlg.help_btn, SIGNAL("clicked()"), self.showHelp)

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
        # remove the toolbar
        del self.toolbar

    def getGeometryTypes(self, gml_file, requested_geometry_types, max_num_objects = False):
        '''determines geometry types and names in bgt-file'''

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
                    if ((not 'Polygon' in geom_types) and 'Polygon' in requested_geometry_types) and ('polygon' in node_name or 'surface' in node_name):
                        geom_types.append('Polygon')
                        geom_names['Polygon'] = geom_name 
                        geom_paths['Polygon'] = ogr_el_path[:-1]
                    elif ((not 'LineString' in geom_types) and 'LineString' in requested_geometry_types) and 'linestring' in node_name:
                        geom_types.append('LineString')
                        geom_names['LineString'] = geom_name
                        geom_paths['LineString'] = ogr_el_path[:-1]
                    elif ((not 'Point' in geom_types) and 'Point' in requested_geometry_types) and 'point' in node_name:
                        geom_types.append('Point')
                        geom_names['Point'] = geom_name
                        geom_paths['Point'] = ogr_el_path[:-1]
                if len(geom_types) == num_requested_geom_types:
                    return geom_names, geom_paths
        except Exception as v:
            QgsMessageLog.logMessage(u'Error parsing gml: ' + str(v), 'BGTImport')

        return geom_names, geom_paths

    def chooseFile(self):
        """Reacts on browse button and opens the right file selector dialog"""

        self.fileNames = ';'.join(QFileDialog.getOpenFileNames(caption = self.tr(u"Select BGT gml file(s)"), directory = '', filter = '*.gml'))
        self.dlg.fileNameBox.setText(self.fileNames)

    def showHelp(self):
        """Reacts on help button"""

        #qgis.utils.showPluginHelp(filename = 'help/index')
        webbrowser.open_new(os.path.join("file://",os.path.abspath(self.plugin_dir), 'help/build/html','index.html')) 

    def run(self):
        """Import and optionally add chosen files"""
        
        self.dlg.show()
        result = self.dlg.exec_()
        if result:
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

            self.iface.messageBar().pushMessage('INFO', self.tr(u'Start') + ' ' + self.tr(u'Importing BGT gml files ...'))
            progressMessageBar = self.iface.messageBar().createMessage(self.tr(u'Importing BGT gml files ...'))
            bar = QProgressBar()
            bar.setRange(0,0)
            bar.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            progressMessageBar.layout().addWidget(bar)
            self.iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)

            # test symlinking
            _can_symlink = can_symlink(os.path.abspath(os.path.dirname(file_names_list[0])))

            # import the files
            count = 0
            for file_name in file_names_list:
                count = count + 1
                progressMessageBar.setText(self.tr(u"Analyzing file ") + str(count) + self.tr(u" from ") + str(number_of_files) + ": " + os.path.basename(file_name))
                # find the ogr paths to the requested geometries
                geom_names, geom_paths = self.getGeometryTypes(file_name, geometry_types, max_num_objects)

                if len(geom_paths) == 0:
                    self.iface.messageBar().pushMessage('Error', self.tr(u"Could not find any of the requested geometries in: " + os.path.basename(file_name)), level=QgsMessageBar.WARNING)
                else: 
                    for geom_type, geom_path in geom_paths.items():
                        geom_name = geom_path[0]
                        progressMessageBar.setText(self.tr(u"Importing file ") + str(count) + self.tr(u" from ") + str(number_of_files) + ": " + os.path.basename(file_name))

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
                            self.iface.messageBar().pushMessage('Error', self.tr(u"Error in creating gml copies for import: ") + str(v), level=QgsMessageBar.WARNING)  
                            QgsMessageLog.logMessage(u'Error in creating gml copies for import: ' + str(v), 'BGTImport')
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
                                self.iface.messageBar().pushMessage('Error', self.tr(u"Error in reading import definitions: ") + str(v), level=QgsMessageBar.WARNING)  
                                QgsMessageLog.logMessage(u'Error in reading import definitions: ' + str(v), 'BGTImport')
                            else:
                                gfs_fragment = "<GeomPropertyDefn><Name>%s</Name><ElementPath>%s</ElementPath><Type>%s</Type></GeomPropertyDefn>" % (geom_name,'|'.join(geom_path),geom_type)
                                gfs = gfs.replace('<GMLFeatureClass>','<GMLFeatureClass>' + gfs_fragment)

                                try:
                                    with open(gfs_name,'w') as f:
                                        f.write(gfs)
                                except Exception as v:
                                    self.iface.messageBar().pushMessage('Error', self.tr(u"Error in writing import definitions: ") + str(v), level=QgsMessageBar.WARNING)  
                                    QgsMessageLog.logMessage(u'Error in writing import definitions: ' + str(v), 'BGTImport')
                                else:
                                    if self.dlg.add_cbx.isChecked():
                                        progressMessageBar.setText(self.tr(u"Adding file ") + str(count) + self.tr(u" from ") + str(number_of_files) + ": " + os.path.basename(gml_name))
                                        self.iface.addVectorLayer(gml_name,os.path.basename(file_name)[:-4],'ogr')

            QApplication.restoreOverrideCursor()

            progressMessageBar.setText(self.tr(u"Importing BGT gml files done!"))
            bar.setRange(0,100)
            bar.setValue(100)

