'''
Uitility functions for working with the BGT.
'''

import argparse
import os
import shutil
import tempfile
import urllib.request
import uuid
import zipfile

from osgeo import gdal
from osgeo import ogr
from osgeo import osr

try:
    from qgis.core import Qgis, QgsTask, QgsTaskManager, QgsMessageLog
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
        'bgt_ongeclassificeerdobject_P'
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


def download_tiles(task, tiles, file_name, nam = None):
    '''
    Downloads the tiles from the BGT server and saves the zip as file_name.
    
    Required parameters:
    
    - `task`            a QgsTask provided by QgsTaskManager. 
                        `None` will do fine when no taskmanager is used.
    - `tiles`           an iterable containing BGT tile numbers.
    - `file_name`       the file name as which the downloaded zip will be saved.
    
    Optional parameters:
    
    - `nam`             An urllib compatible QgsNetworkAccessManager.
                        You should use this when running from QGIS.
                        When not provided urllib is used for downloads, which
                        is fine when not run from QGIS.

    Returns:

    `file_name`         the file name as which the downloaded zip was saved.
    '''
    
    if task:
        QgsMessageLog.logMessage(u'Start downloading BGT-tiles: ' + str(tiles),
            tag = 'BGTImport', level = Qgis.Info)
        task.setProgress(5)

    encoded_url = "https://downloads.pdok.nl/service/extract.zip?" +\
      "extractname=bgt&extractset=citygml&excludedtypes=plaatsbepalingspunt&history=true&" +\
      "tiles=%7B%22layers%22%3A%5B%7B%22aggregateLevel%22%3A0%2C%22codes%22%3A%5B" + \
      '%2C'.join([str(x) for x in tiles]) + "%5D%7D%5D%7D"
    try:  
        if os.path.exists(file_name):
            os.remove(file_name)
        if nam:
            (response, content) = nam.request(encoded_url, task = task)
            with open(file_name,'wb') as f:
                f.write(content)
        else:
            with urllib.request.urlopen(encoded_url) as response:
                with open(file_name,'wb') as f:
                    f.write(response.read())
        if task:
            QgsMessageLog.logMessage(u'Done downloading BGT-tiles',
                tag = 'BGTImport', level = Qgis.Info)
            task.setProgress(100)
        return True
    except Exception as v:
        if task:
            QgsMessageLog.logMessage(u'Error downloading BGT-tiles: ' + str(v),
                tag = 'BGTImport', level = Qgis.Critical)
        return False


def import_to_geopackage(task, zip_file_name, geopackage):
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
    
    Returns:
    
    - `geopackage`      the file name of the geopackage.
    '''


    progress = 10
    if task:
        QgsMessageLog.logMessage(u'Start importing BGT-zip: ' + str(zip_file_name),
            tag = 'BGTImport', level = Qgis.Info)
        task.setProgress(progress)
    gdal.UseExceptions()
    gfs_folder = os.path.join(os.path.dirname(__file__), 'gfs')
    
    try:
        # have a copy of the zip file available next to the gopackage
        # so we can check the gml files if needed
        if not os.path.exists(geopackage.replace('.gpkg','.zip')):
            shutil.copy(zip_file_name, geopackage.replace('.gpkg','.zip'))
    except:
        pass
    
    try:
        tmp_dir = tempfile.TemporaryDirectory()
        if os.path.exists(geopackage):
            os.remove(geopackage)
        gp = ogr.GetDriverByName('GPKG').CreateDataSource(geopackage)
        #gp =  ogr.GetDriverByName('GPKG').Open( geopackage, update = 1 )
        with tmp_dir:
            tmp_folder = tmp_dir.name
            with zipfile.ZipFile(zip_file_name, "r") as f:
                f.extractall(tmp_folder)
                increment = 80 / len(f.infolist()) 
                for info in f.infolist(): 
                    base_name = os.path.basename(info.filename)
                    QgsMessageLog.logMessage(u'Importing from BGT-zip: ' + str(base_name), 
                            tag = 'BGTImport', level = Qgis.Info)
                    for postfix in ['_V','_L','_P']:
                        gfs_file_name = base_name.replace('.gml', postfix + '.gfs')
                        if os.path.exists(os.path.join(gfs_folder, gfs_file_name)):
                            if task:
                                QgsMessageLog.logMessage(u'Importing from BGT-zip: ' \
                                    + u'...' + str(base_name) + str(postfix),
                                    tag = 'BGTImport', level = Qgis.Info)
                            shutil.copyfile(os.path.join(gfs_folder, gfs_file_name),
                                os.path.join(tmp_folder, base_name.replace('.gml','.gfs')))
                            ds = ogr.GetDriverByName('gml').Open(os.path.join(tmp_folder, base_name))
                            input_layer = ds.GetLayer()
                            if input_layer.GetFeatureCount():
                                new_layer = gp.CopyLayer(input_layer, 
                                    base_name.replace('.gml', postfix))
                                del new_layer
                            del input_layer, ds
                    progress = progress + increment
                    if task:
                        task.setProgress(progress)
        del gp # dereference is needed to close and save the file
        if task:
            task.setProgress(100)
            QgsMessageLog.logMessage(u'Done importing BGT-zip: ' + str(zip_file_name), 
                tag = 'BGTImport', level = Qgis.Info)
        return geopackage
    except Exception as v:
        if task:
            QgsMessageLog.logMessage(u'Error importing BGT-zip: ' + str(v), 
                tag = 'BGTImport', level = Qgis.Critical)
        return False


if __name__ == "__main__":
    pass
    # todo: add command line interface
    
