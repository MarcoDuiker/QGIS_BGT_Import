'''
Uitility functions for working with the BGT.
'''

import argparse
import os
import shutil
import sys
import tempfile
import urllib.request
import uuid
import zipfile

from copy import deepcopy

from osgeo import gdal
from osgeo import ogr
from osgeo import osr

import xml.etree.ElementTree as ET

try:
    from qgis.core import Qgis, QgsTask, QgsTaskManager, QgsMessageLog
except:
    pass

try:
    # this gives us a (much) faster end cleaner implementation
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
        # have a copy of the zip file available next to the geopackage
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
                                    + u'...' + str(base_name) + str(postfix),
                                    tag = 'BGTImport', level = Qgis.Info)
                            shutil.copyfile(os.path.join(gfs_folder, gfs_file_name),
                                os.path.join(tmp_folder, base_name.replace('.gml','.gfs')))
                            ds = ogr.GetDriverByName('gml').Open(os.path.join(tmp_folder, base_name))
                            input_layer = ds.GetLayer()
                            if postfix == '_V':
                                
                                input_layer.SetAttributeFilter("OGR_GEOMETRY='Polygon'")
                            elif postfix == '_L':
                                input_layer.SetAttributeFilter("OGR_GEOMETRY='LineString'")
                            elif postfix == '_P':
                                input_layer.SetAttributeFilter("OGR_GEOMETRY='Point'")
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
    
