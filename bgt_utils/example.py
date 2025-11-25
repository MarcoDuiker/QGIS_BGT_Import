# -*- coding: utf-8 -*-

'''
Example script for working with the BGT outside or even without QGIS.
'''

import utils as bgt_utils

# example import statements when using this script in a different
# environment than this local folder:
# import bgt_utils.utils as bgt_utils
# from .bgt_utils import utils as bgt_utils


# When QGIS is present we can download a BGT zip from the download API
# Don't forget to adapt `QGIS_PATH` with the actual path to the 
# QGIS installation. 
# See: https://docs.qgis.org/3.40/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts

QGIS_PATH = "/usr/bin/qgis"
QGIS_AVAILABLE = False
try:
    from qgis.core import *
    QgsApplication.setPrefixPath(QGIS_PATH, True)
    qgs = QgsApplication([], False)
    qgs.initQgis()
    QGIS_AVAILABLE = True
    
if QGIS_AVAILABLE:
    zip_file = bgt_utils.download_zip(
        task = None,
        file_name = "example.zip",
        geofilter = "POLYGON ((155039 463024, 155039 463278, 155326 463278, 155326 463024, 155039 463024))" 
    )

# Without QGIS present on system we can convert a BGT-zip to a 
# geopackage without data loss.
zip_file = "example.zip"
gpkg_file = bgt_utils.import_to_geopackage(
    task = None,
    zip_file_name = zip_file,
    geopackage = "example.gpkg" )

if QGIS_AVAILABLE:
    qgs.exitQgis()
