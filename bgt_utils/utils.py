'''
Utility functions for working with the BGT.
'''

import argparse
import json
import logging
import os
import requests
import shutil
import sys
import tempfile
import urllib.request
import uuid
import zipfile

from copy import deepcopy
from time import sleep

from osgeo import gdal
from osgeo import ogr
from osgeo import osr

import xml.etree.ElementTree as ET

ogr.UseExceptions() 

try:
    QGIS_NETWORKING = True
    # We MAY and MUST use QGIS networking to respect all network
    # settings in QGIS
    
    from qgis.core import Qgis, QgsTask, QgsTaskManager, QgsMessageLog,\
      QgsBlockingNetworkRequest, QgsFileDownloader, QgsNetworkContentFetcher
      
    from qgis.PyQt.QtNetwork import QNetworkReply, QNetworkRequest
    from qgis.PyQt.QtCore import QUrl, QEventLoop

    
except:
    QGIS_NETWORKING = False
    # This module is used from outside QGIS.
    # We CANNOT use QGIS networking

try:
    # this gives us a (much) faster and cleaner implementation
    # on the openbare ruimtelabel verwerking
    import lxml
    from lxml import etree
except:
    pass
    
    
__author__ = 'Marco Duiker MD-kwadraat'
__date__ = 'October 2018'

def get_standard_layers():
    '''
    Returns a nice order for all the layers known to the QGIS plugin.
    '''
    
    return [
        'bgt_bak_P',
        'bgt_bord_P',
        'bgt_installatie_P',
        'bgt_kast_P',
        'bgt_kunstwerkdeel_P',
        'bgt_mast_P',
        'bgt_openbareruimtelabel_P',
        'bgt_paal_P',
        'bgt_pand_P',
        'bgt_put_P',
        'bgt_sensor_P',
        'bgt_straatmeubilair_P',
        'bgt_vegetatieobject_P',
        'bgt_waterinrichtingselement_P',
        'bgt_weginrichtingselement_P',
        'bgt_ongeclassificeerdobject_P',
        'bgt_begroeidterreindeel_L',
        'bgt_onbegroeidterreindeel_L',
        'bgt_ondersteunendwegdeel_L',
        'bgt_scheiding_L',
        'bgt_spoor_L',
        'bgt_vegetatieobject_L',
        'bgt_waterinrichtingselement_L',
        'bgt_wegdeel_L',
        'bgt_weginrichtingselement_L',
        'bgt_ongeclassificeerdobject_L',
        'bgt_overbruggingsdeel_V',
        'bgt_functioneelgebied_V',
        'bgt_gebouwinstallatie_V',
        'bgt_overigbouwwerk_V',
        'bgt_pand_V',
        'bgt_overigescheiding_L',
        'bgt_overigescheiding_V',
        'bgt_scheiding_V',
        'bgt_vegetatieobject_V',
        'bgt_weginrichtingselement_V',
        'bgt_tunneldeel_V',
        'bgt_wegdeel_V',
        'bgt_ondersteunendwegdeel_V',
        'bgt_ondersteunendwaterdeel_V',
        'bgt_begroeidterreindeel_V',
        'bgt_onbegroeidterreindeel_V',
        'bgt_kunstwerkdeel_L',
        'bgt_kunstwerkdeel_V',
        'bgt_waterdeel_V',
        'bgt_ongeclassificeerdobject_V']
        
def get_visible_layers():
    '''
    Returns a list of layers which should be 'on'.
    '''
    
    return [
        'bgt_kunstwerkdeel_P',
        'bgt_openbareruimtelabel_P',
        'bgt_pand_P',
        'bgt_vegetatieobject_P',
        'bgt_scheiding_L',
        'bgt_spoor_L',
        'bgt_overbruggingsdeel_V',
        'bgt_functioneelgebied_V',
        'bgt_gebouwinstallatie_V',
        'bgt_overigbouwwerk_V',
        'bgt_pand_V',
        'bgt_overigescheiding_L',
        'bgt_overigescheiding_V',
        'bgt_scheiding_V',
        'bgt_weginrichtingselement_V',
        'bgt_tunneldeel_V',
        'bgt_wegdeel_V',
        'bgt_ondersteunendwegdeel_V',
        'bgt_ondersteunendwaterdeel_V',
        'bgt_begroeidterreindeel_V',
        'bgt_onbegroeidterreindeel_V',
        'bgt_kunstwerkdeel_L',
        'bgt_kunstwerkdeel_V',
        'bgt_waterdeel_V',
        'bgt_ongeclassificeerdobject_V']
        
def get_featuretypes():
    '''
    Returns a list of all BGT featuretypes
    '''
    
    return [    "bak",
                "begroeidterreindeel",
                "bord",
                "buurt",
                "functioneelgebied",
                "gebouwinstallatie",
                "installatie",
                "kast",
                "kunstwerkdeel",
                "mast",
                "onbegroeidterreindeel",
                "ondersteunendwaterdeel",
                "ondersteunendwegdeel",
                "ongeclassificeerdobject",
                "openbareruimte",
                "openbareruimtelabel",
                "overbruggingsdeel",
                "overigbouwwerk",
                "overigescheiding",
                "paal",
                "pand",
                "put",
                "scheiding",
                "sensor",
                "spoor",
                "stadsdeel",
                "straatmeubilair",
                "tunneldeel",
                "vegetatieobject",
                "waterdeel",
                "waterinrichtingselement",
                "waterschap",
                "wegdeel",
                "weginrichtingselement",
                "wijk" ]



def download_zip(task, file_name, geofilter, featuretypes = get_featuretypes()):
    '''
    Downloads the tiles from the BGT server and saves the zip as file_name.
    Must be called from within QGIS.
    Alternatively the download can be done via the BGT download viewer.
    
    Required parameters:
    
    - `task`            a QgsTask provided by QgsTaskManager. 
                        `None` will do fine when no taskmanager is used.
    - `geofilter`       a polygon in WKT format.
    - `file_name`       the file name as which the downloaded zip will be saved.
    
    Optional parameters:
    
    - `featuretypes`    The featuretypes to request. If not provided
                        the default set with all BGT featuretypes 
                        will be used.

    Returns:

    `file_name`         the file name as which the downloaded zip was saved.
    '''
    
    if not QGIS_NETWORKING:
        raise NotImplementedError("Download can only be done from with QGIS.")
    
    API_url = "https://api.pdok.nl"
    prepare_download_url = API_url + "/lv/bgt/download/v1_0/full/custom"
    post_params = { "format":           "citygml",
                    "featuretypes":     featuretypes,
                    "geofilter":        geofilter }
                    
    def show_download_progress(bytesReceived, bytesTotal):
        progress = round(bytesReceived/ bytesTotal)
        if progress < 100:
            task.setProgress(progress)
        
    progress = 0
    if task:
        task.setProgress(progress)
    
    QgsMessageLog.logMessage(u'Start preparing BGT-zip',
        tag = 'BGTImport', level = Qgis.Info)
    
    request = QgsBlockingNetworkRequest()
    req = QNetworkRequest(QUrl(prepare_download_url))
    req.setHeader(  QNetworkRequest.KnownHeaders.ContentTypeHeader, 
                    'application/json')
    err = request.post(req, bytes(json.dumps(post_params), 'utf-8'))
    if err == QgsBlockingNetworkRequest.ErrorCode.NoError:
        resp = request.reply()
        QgsMessageLog.logMessage(u'API response: ' + str(
            resp.content(), encoding='utf-8'),
            tag = 'BGTImport', level = Qgis.Info)
        json_resp = json.loads(resp.content().data())
        
        status_request = QgsBlockingNetworkRequest()
        status_req = QNetworkRequest(QUrl(API_url + 
            json_resp["_links"]["status"]["href"]))
            
        status = "PENDING"
        while status == "RUNNING" \
        or    status == "PENDING":
            sleep(1)
            err = status_request.get(status_req, forceRefresh = True)
            if err == QgsBlockingNetworkRequest.ErrorCode.NoError:
                status_msg = json.loads(
                                status_request.reply().content().data())
                status = status_msg['status']
                if task:
                    task.setProgress(status_msg['progress'])
            else:
                QgsMessageLog.logMessage(u'API error: ' + \
                    status_request.errorMessage(),
                    tag = 'BGTImport', level = Qgis.Critical)
                return
                
        if status_msg['status'] == "COMPLETED":
            download_url = API_url + \
                           status_msg["_links"]["download"]["href"]
            QgsMessageLog.logMessage(
                u'BGT-zip is prepared. Starting download from: ' + \
                download_url,
                tag = 'BGTImport', level = Qgis.Info)
            if task:
                download_request = QgsBlockingNetworkRequest()
                download_request.downloadProgress.connect(
                                        show_download_progress)
                err = download_request.get(
                            QNetworkRequest(QUrl(download_url)))
                if err == QgsBlockingNetworkRequest.ErrorCode.NoError:
                    with open(file_name, 'wb') as f:
                        f.write(download_request.reply().content())
                        return file_name
                else:
                    QgsMessageLog.logMessage(u'Download error: ' + \
                    download_request.errorMessage(),
                    tag = 'BGTImport', level = Qgis.Critical)
            else:
                # for test purposes when not having a task
                loop = QEventLoop()
                dl = QgsFileDownloader(QUrl(download_url), file_name)
                dl.downloadExited.connect(loop.quit)
                dl.startDownload()
                loop.exec_()
                return file_name
        else: 
            QgsMessageLog.logMessage(u'Preparation of download failed: ' + \
                    status_msg['status'],
                    tag = 'BGTImport', level = Qgis.Critical)   
    else:
        QgsMessageLog.logMessage(u'API error: ' + \
            request.errorMessage(),
            tag = 'BGTImport', level = Qgis.Critical)
            
def get_postgis_driver(connection_string):
    '''
    Returns a postgis driver from the given coonection string
    
    a connection string has the well known format like:
    "PG: host=%s dbname=%s user=%s password=%s schema=%s"
    '''

    return ogr.Open(connection_string)
    
def get_geopackage_driver(geopackage):
    '''
    Returns a geopackage driver from the given geopackage file path.
    '''
    
    if os.path.exists(geopackage):
            os.remove(geopackage)
    return ogr.GetDriverByName('GPKG').CreateDataSource(geopackage)
    
def import_to_geopackage(task, zip_file_name, geopackage, progress_bar = None):
    '''
    Imports the gml files from BGT zip into one geopackage.
    
    The import uses prepared gfs files to read all available geometry types
    completely, and to apply the right coordinate reference system.
    
    Required parameters:
    
    - `task`            a QgsTask provided by QgsTaskManager. 
                        `None` will do fine when no taskmanager is used.
    - `tiles`           an iterable containing BGT tile numbers.
    - `zip_file_name`   the file name of the BGT zip file.
    - `geopackage`      file name of the geopackage to import to.
    - `progress_bar`    an object instance having a setValue method 
                        accepting values between 0 and 100 to indicate 
                        progress.
                        A QProgressBar() as available in QGIS will do.
    Returns:
    
    - `geopackage`      the file name of the geopackage.
    '''
    
    try:
        # have a copy of the zip file available next to the geopackage
        # so we can check the gml files if needed
        if not os.path.exists(geopackage.replace('.gpkg','.zip')):
            shutil.copy(zip_file_name, geopackage.replace('.gpkg','.zip'))
    except:
        pass
    
    driver = get_geopackage_driver(geopackage)
    import_to_driver(task, zip_file_name, driver, progress_bar = None)
    
    return geopackage
    
def import_to_postgis(task, zip_file_name, connection_string, progress_bar = None):
    '''
    Imports the gml files from BGT zip into a postgis schmema.
    
    The import uses prepared gfs files to read all available geometry types
    completely, and to apply the right coordinate reference system.
    
    Required parameters:
    
    - `task`            a QgsTask provided by QgsTaskManager. 
                        `None` will do fine when no taskmanager is used.
    - `tiles`           an iterable containing BGT tile numbers.
    - `zip_file_name`   the file name of the BGT zip file.
    - `geopackage`      file name of the geopackage to import to.
    - `progress_bar`    an object instance having a setValue method 
                        accepting values between 0 and 100 to indicate 
                        progress.
                        A QProgressBar() as available in QGIS will do.
    Returns:
    
    - `True`            when no exceptions
    - `False`           on exceptions
    '''
    
    driver = get_geopackage_driver(connection_string)
    return import_to_driver(task, zip_file_name, driver, progress_bar = None)
    
def import_to_driver(task, zip_file_name, driver, progress_bar = None):
    '''
    Imports the gml files from BGT zip into an ogr driver.
    
    The import uses prepared gfs files to read all available geometry types
    completely, and to apply the right coordinate reference system.
    
    The driver will be closed at the end of the import.
    
    Required parameters:
    
    - `task`            a QgsTask provided by QgsTaskManager. 
                        `None` will do fine when no taskmanager is used.
    - `tiles`           an iterable containing BGT tile numbers.
    - `zip_file_name`   the file name of the BGT zip file.
    - `driver`          an open ogr driver
    - `progress_bar`    an object instance having a setValue method 
                        accepting values between 0 and 100 to indicate 
                        progress.
                        A QProgressBar() as available in QGIS will do.
    Returns:
    
    - `True`            when no exceptions
    - `False`           on exceptions
    '''


    progress = 10
    if task:
        QgsMessageLog.logMessage(u'Start importing BGT-zip: ' + str(zip_file_name),
            tag = 'BGTImport', level = Qgis.Info)
        task.setProgress(progress)
    if progress_bar:
        progress_bar.setValue(progress)
            
    gdal.UseExceptions()
    gfs_folder = os.path.join(os.path.dirname(__file__), 'gfs')
    
    try:
        with tempfile.TemporaryDirectory() as tmp_folder:
            with zipfile.ZipFile(zip_file_name, "r") as f:
                f.extractall(tmp_folder)
                increment = 80 / len(f.infolist()) 
                for info in f.infolist(): 
                    base_name = os.path.basename(info.filename)

                    # temporary fix for: https://github.com/MarcoDuiker/QGIS_BGT_Import/issues/19
                    add_srs_dimension(task, base_name, tmp_folder)

                    if task:
                        QgsMessageLog.logMessage(u'Importing from BGT-zip: ' \
                            + str(base_name), tag = 'BGTImport', level = Qgis.Info)
                    if base_name == 'bgt_openbareruimtelabel.gml':
                        if task:
                            QgsMessageLog.logMessage(u'Start processing OpenbareRuimteLabel.', 
                            tag = 'BGTImport', level = Qgis.Info)
                        if 'lxml' in globals():
                            _process_ORL(task, base_name, tmp_folder)
                        else:
                            _process_ORL_ugly(task, base_name, tmp_folder)
                    for postfix in ['_V','_L','_P']:
                        gfs_file_name = base_name.replace('.gml', postfix + '.gfs')
                        if os.path.exists(os.path.join(gfs_folder, gfs_file_name)):
                            if task:
                                QgsMessageLog.logMessage(u'Importing from BGT-zip: ' \
                                    + u'...' + str(base_name).replace('.gml', '%s.gml '% str(postfix)),
                                    tag = 'BGTImport', level = Qgis.Info)
                            copy_ok = shutil.copyfile(os.path.join(gfs_folder, gfs_file_name),
                                os.path.join(tmp_folder, base_name.replace('.gml','.gfs')))
                            if copy_ok:
                                try:
                                    ds = ogr.GetDriverByName('gml').Open(os.path.join(tmp_folder, base_name))
                                    # with ogr.GetDriverByName('gml').Open(os.path.join(tmp_folder, base_name)) as ds:  # available from gdal 3.8)
                                    input_layer = ds.GetLayer()
                                    if task:
                                        QgsMessageLog.logMessage(u'Succesfully opened: ' \
                                            + str(base_name).replace('.gml', '%s.gml '% str(postfix)) , 
                                            tag = 'BGTImport', level = Qgis.Info)
                                    geom_col_name = input_layer.GetGeometryColumn()
                                    if not geom_col_name:
                                        geom_col_name = "_ogr_geometry_"
                                    if postfix == '_V':
                                        input_layer.SetAttributeFilter('''OGR_GEOMETRY='MultiSurface' and "%s" IS NOT NULL''' % geom_col_name)
                                    elif postfix == '_L':
                                        input_layer.SetAttributeFilter('''OGR_GEOMETRY='MultiCurve' and "%s" IS NOT NULL''' % geom_col_name)
                                    elif postfix == '_P':
                                        input_layer.SetAttributeFilter('''OGR_GEOMETRY='MultiPoint' and "%s" IS NOT NULL''' % geom_col_name)
                                    if input_layer.GetFeatureCount():
                                        new_layer = driver.CopyLayer(input_layer, 
                                            base_name.replace('.gml', postfix))
                                        new_layer.SyncToDisk()
                                        new_layer = None
                                        if task:
                                          QgsMessageLog.logMessage(u'Succesfully copied: ' \
                                              + str(base_name) + str(postfix) , 
                                              tag = 'BGTImport', level = Qgis.Info)
                                    #del input_layer, ds
                                    input_layer = None
                                    ds = None
                                except Exception as v:
                                    if task:
                                        QgsMessageLog.logMessage(u'Error importing: ' \
                                            + str(base_name) + str(postfix) + " " + str(v), 
                                            tag = 'BGTImport', level = Qgis.Warning)
                            else:
                                if task:
                                  QgsMessageLog.logMessage(u'Failed to copy: ' \
                                      + str(os.path.join(gfs_folder, gfs_file_name)) + "to" \
                                      + str(os.path.join(tmp_folder, base_name.replace('.gml','.gfs'))),
                                      tag = 'BGTImport', level = Qgis.Warning)
                    progress = progress + increment
                    if task:
                        task.setProgress(progress)
                    if progress_bar:
                        progress_bar.setValue(progress)
            sleep(1)    # just to be sure
            #del gp     # dereference is needed to close and save the file
            driver = None   # dereference is needed to close and save the file
        if task:
            task.setProgress(100)
            QgsMessageLog.logMessage(u'Done importing BGT-zip: ' + str(zip_file_name), 
                tag = 'BGTImport', level = Qgis.Info)
        if progress_bar:
            progress_bar.setValue(progress)
        return True
    except Exception as v:
        if task:
            QgsMessageLog.logMessage(u'Error importing BGT-zip: ' + str(v), 
                tag = 'BGTImport', level = Qgis.Critical)
        return False
    

def import_to_geopackage_old(task, zip_file_name, geopackage, progress_bar = None):
    '''
    Imports the gml files from BGT zip into one geopackage.
    
    The import uses prepared gfs files to read all available geometry types
    completely, and to apply the right coordinate reference system.
    
    Required parameters:
    
    - `task`            a QgsTask provided by QgsTaskManager. 
                        `None` will do fine when no taskmanager is used.
    - `tiles`           an iterable containing BGT tile numbers.
    - `zip_file_name`   the file name of the BGT zip file.
    - `geopackage`      file name of the geopackage to import to.
    - `progress_bar`    an object instance having a setValue method 
                        accepting values between 0 and 100 to indicate 
                        progress.
                        A QProgressBar() as available in QGIS will do.
    Returns:
    
    - `geopackage`      the file name of the geopackage.
    '''


    progress = 10
    if task:
        QgsMessageLog.logMessage(u'Start importing BGT-zip: ' + str(zip_file_name),
            tag = 'BGTImport', level = Qgis.Info)
        task.setProgress(progress)
    if progress_bar:
        progress_bar.setValue(progress)
            
    gdal.UseExceptions()
    gfs_folder = os.path.join(os.path.dirname(__file__), 'gfs')
    
    try:
        # have a copy of the zip file available next to the geopackage
        # so we can check the gml files if needed
        if not os.path.exists(geopackage.replace('.gpkg','.zip')):
            shutil.copy(zip_file_name, geopackage.replace('.gpkg','.zip'))
    except:
        pass
    
    try:
        if os.path.exists(geopackage):
            os.remove(geopackage)
        gp = ogr.GetDriverByName('GPKG').CreateDataSource(geopackage)
        with tempfile.TemporaryDirectory() as tmp_folder:
            with zipfile.ZipFile(zip_file_name, "r") as f:
                f.extractall(tmp_folder)
                increment = 80 / len(f.infolist()) 
                for info in f.infolist(): 
                    base_name = os.path.basename(info.filename)

                    # temporary fix for: https://github.com/MarcoDuiker/QGIS_BGT_Import/issues/19
                    add_srs_dimension(task, base_name, tmp_folder)

                    if task:
                        QgsMessageLog.logMessage(u'Importing from BGT-zip: ' \
                            + str(base_name), tag = 'BGTImport', level = Qgis.Info)
                    if base_name == 'bgt_openbareruimtelabel.gml':
                        if task:
                            QgsMessageLog.logMessage(u'Start processing OpenbareRuimteLabel.', 
                            tag = 'BGTImport', level = Qgis.Info)
                        if 'lxml' in globals():
                            _process_ORL(task, base_name, tmp_folder)
                        else:
                            _process_ORL_ugly(task, base_name, tmp_folder)
                    for postfix in ['_V','_L','_P']:
                        gfs_file_name = base_name.replace('.gml', postfix + '.gfs')
                        if os.path.exists(os.path.join(gfs_folder, gfs_file_name)):
                            if task:
                                QgsMessageLog.logMessage(u'Importing from BGT-zip: ' \
                                    + u'...' + str(base_name).replace('.gml', '%s.gml '% str(postfix)),
                                    tag = 'BGTImport', level = Qgis.Info)
                            copy_ok = shutil.copyfile(os.path.join(gfs_folder, gfs_file_name),
                                os.path.join(tmp_folder, base_name.replace('.gml','.gfs')))
                            if copy_ok:
                                try:
                                    ds = ogr.GetDriverByName('gml').Open(os.path.join(tmp_folder, base_name))
                                    # with ogr.GetDriverByName('gml').Open(os.path.join(tmp_folder, base_name)) as ds:  # available from gdal 3.8)
                                    input_layer = ds.GetLayer()
                                    if task:
                                        QgsMessageLog.logMessage(u'Succesfully opened: ' \
                                            + str(base_name).replace('.gml', '%s.gml '% str(postfix)) , 
                                            tag = 'BGTImport', level = Qgis.Info)
                                    geom_col_name = input_layer.GetGeometryColumn()
                                    if not geom_col_name:
                                        geom_col_name = "_ogr_geometry_"
                                    if postfix == '_V':
                                        input_layer.SetAttributeFilter('''OGR_GEOMETRY='MultiSurface' and "%s" IS NOT NULL''' % geom_col_name)
                                    elif postfix == '_L':
                                        input_layer.SetAttributeFilter('''OGR_GEOMETRY='MultiCurve' and "%s" IS NOT NULL''' % geom_col_name)
                                    elif postfix == '_P':
                                        input_layer.SetAttributeFilter('''OGR_GEOMETRY='MultiPoint' and "%s" IS NOT NULL''' % geom_col_name)
                                    if input_layer.GetFeatureCount():
                                        new_layer = gp.CopyLayer(input_layer, 
                                            base_name.replace('.gml', postfix))
                                        new_layer.SyncToDisk()
                                        new_layer = None
                                        if task:
                                          QgsMessageLog.logMessage(u'Succesfully copied into gpkg: ' \
                                              + str(base_name) + str(postfix) , 
                                              tag = 'BGTImport', level = Qgis.Info)
                                    #del input_layer, ds
                                    input_layer = None
                                    ds = None
                                except Exception as v:
                                    if task:
                                        QgsMessageLog.logMessage(u'Error importing: ' \
                                            + str(base_name) + str(postfix) + " " + str(v), 
                                            tag = 'BGTImport', level = Qgis.Warning)
                            else:
                                if task:
                                  QgsMessageLog.logMessage(u'Failed to copy: ' \
                                      + str(os.path.join(gfs_folder, gfs_file_name)) + "to" \
                                      + str(os.path.join(tmp_folder, base_name.replace('.gml','.gfs'))),
                                      tag = 'BGTImport', level = Qgis.Warning)
                    progress = progress + increment
                    if task:
                        task.setProgress(progress)
                    if progress_bar:
                        progress_bar.setValue(progress)
        sleep(1)    # just to be sure
        #del gp     # dereference is needed to close and save the file
        gp = None   # dereference is needed to close and save the file
        if task:
            task.setProgress(100)
            QgsMessageLog.logMessage(u'Done importing BGT-zip: ' + str(zip_file_name), 
                tag = 'BGTImport', level = Qgis.Info)
        if progress_bar:
            progress_bar.setValue(progress)
        return geopackage
    except Exception as v:
        if task:
            QgsMessageLog.logMessage(u'Error importing BGT-zip: ' + str(v), 
                tag = 'BGTImport', level = Qgis.Critical)
        return False

def add_srs_dimension(task, gml_file_name, tmp_folder):
    '''
    A quick and dirty function to add srsDimension to a posList if not already there.
    see: https://github.com/MarcoDuiker/QGIS_BGT_Import/issues/19
    '''

    gml_file = os.path.join(tmp_folder, gml_file_name)
    with open(gml_file, encoding="utf-8") as f:
        txt = f.read().replace("<gml:posList>", '<gml:posList srsDimension="2">')
    with open(gml_file, mode = 'w', encoding="utf-8") as f:
        f.write(txt)


def _duplicateOrl(xf, elem):
    '''
    A private helper function for the processing of openbareruimte labels.
    
    Adapted from NLExtract.
    '''

    out_elem = deepcopy(elem)
    ns = {'imgeo': 'http://www.geostandaarden.nl/imgeo/2.1'}
    count = int(out_elem.xpath('count(//imgeo:positie)', namespaces=ns))

    for i in range(0, count):
        out_elem = deepcopy(elem)
        # Remove all position elements except for the i'th. This is done by first collecting all positions into
        # a list, then remove the position from that list which should be kept, and then remove all remaining positions
        # in the list from the XML element.
        positions = out_elem.xpath('//imgeo:positie', namespaces=ns)
        del positions[i]
        for pos in positions:
            pos.getparent().remove(pos)

        xf.write(out_elem)


def _process_ORL(task, orl_gml, tmp_folder):
    '''
    A private helper function to process OpenbareRuimteLabel.
    It duplicate features so that all labels will be shown.

    Adapted from NLExtract.
    '''

    input_gml = os.path.join(tmp_folder, orl_gml)
    temp_file = os.path.join(tmp_folder, 'bgt_orl.gml')

    nsmap = {None: "http://www.opengis.net/citygml/2.0"}

    try:
        with etree.xmlfile(temp_file) as xf:
            with xf.element('{http://www.opengis.net/citygml/2.0}CityModel', nsmap=nsmap):
                with open(input_gml,'rb') as f:
                    context = etree.iterparse(f)
                    for action, elem in context:
                        if action == 'end' and elem.tag == '{http://www.opengis.net/citygml/2.0}cityObjectMember':
                            # Duplicate openbareruimtelabel
                            _duplicateOrl(xf, elem)
                            # Clean up the original element and the node of its previous sibling
                            # (https://www.ibm.com/developerworks/xml/library/x-hiperfparse/)
                            elem.clear()
                            while elem.getprevious() is not None:
                                del elem.getparent()[0]
                    del context
            xf.flush()
    except Exception as v:
        # we'll just keep the original gml with it's limitations
        if task:
            QgsMessageLog.logMessage(u'Error processing openbareruimtelabel: ' + str(v), 
                tag = 'BGTImport', level = Qgis.Info)
        pass
    else:
        shutil.copyfile(temp_file, input_gml)
        if task:
            QgsMessageLog.logMessage(u'Succesfully created a new openbareruimtelabel gml.', 
                                     tag = 'BGTImport', level = Qgis.Info)


def _duplicateOrl_ugly(elem):
    '''
    A private helper function for the processing of openbareruimte labels.
    
    Adapted (a lot) from NLExtract.
    '''

    out_elem = deepcopy(elem)
    ns = {'imgeo': 'http://www.geostandaarden.nl/imgeo/2.1'}
    count = len(out_elem.findall('.//imgeo:positie', namespaces=ns))

    xml_string = ''
    for i in range(0, count):
        out_elem = deepcopy(elem)
        for el in out_elem.iter():
            if el.tag == '{http://www.geostandaarden.nl/imgeo/2.1}Label':
                j=0
                for child in el.getchildren():
                    if child.tag == '{http://www.geostandaarden.nl/imgeo/2.1}positie':
                        if not j == i:
                            el.remove(child) 
                        j = j + 1
        xml_string = xml_string + str(ET.tostring(out_elem, encoding = 'utf-8'))
        
    return xml_string 

def _process_ORL_ugly(task, orl_gml, tmp_folder):
    '''
    A private helper function to process OpenbareRuimteLabel.
    It duplicate features so that all labels will be shown.

    It avoids using lxml as that is a major hassle under windows.
    Of course, this implementation has a small memory footprint but it is rather ugly.
    '''

    input_gml = os.path.join(tmp_folder, orl_gml)
    temp_file = os.path.join(tmp_folder, 'bgt_orl.gml')

    nsmap = {None: "http://www.opengis.net/citygml/2.0"}

    header = '''<?xml version="1.0" encoding="UTF-8"?>
<CityModel xmlns:gml="http://www.opengis.net/gml" xmlns:imgeo="http://www.geostandaarden.nl/imgeo/2.1" xmlns="http://www.opengis.net/citygml/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.geostandaarden.nl/imgeo/2.1 http://schemas.geonovum.nl/imgeo/2.1/imgeo-2.1.1.xsd">'''

    footer = '''</CityModel>'''

    try:
        with open(temp_file, 'w') as xf:
            with open(input_gml,'rb') as f:
                xf.write(header)
                context = ET.iterparse(f)
                for action, elem in context:
                    if action == 'end' and elem.tag == '{http://www.opengis.net/citygml/2.0}cityObjectMember':
                        # Duplicate openbareruimtelabel
                        xf.write(_duplicateOrl_ugly(elem))
                        # Clean up the original element and the node of its previous sibling
                        # (https://www.ibm.com/developerworks/xml/library/x-hiperfparse/)
                        elem.clear()
                del context
            xf.write(footer)
    except Exception as v:
        # we'll just keep the original gml with it's limitations
        if task:
            QgsMessageLog.logMessage(u'Error processing openbareruimtelabel: ' + str(v), 
                tag = 'BGTImport', level = Qgis.Info)
        pass
    else:
        shutil.copyfile(temp_file, input_gml)
        if task:
            QgsMessageLog.logMessage(u'Succesfully created a new openbareruimtelabel gml.', 
                                     tag = 'BGTImport', level = Qgis.Info)


if __name__ == "__main__":
    pass
    # todo: add command line interface
    
