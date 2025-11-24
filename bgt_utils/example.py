# -*- coding: utf-8 -*-

'''
Example script for working with the BGT without QGIS.
'''

import utils as bgt_utils

# example import statements when using this script in a different
# environment than this local folder:

# import bgt_utils.utils as bgt_utils
# from .bgt_utils import utils as bgt_utils

###
# next lines for downloading zip only
#
# uncomment when QGIS is present on the system
# don't forget to replace "/usr/bin/qgis" with the actual path to the 
# QGIS installation. See: https://docs.qgis.org/3.40/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts

# from qgis.core import *
# QgsApplication.setPrefixPath("/usr/bin/qgis", True)
# qgs = QgsApplication([], False)
# qgs.initQgis()

# zip_file = bgt_utils.download_zip(
    # task = None,
    # file_name = "example.zip",
    # geofilter = "POLYGON ((155039 463024, 155039 463278, 155326 463278, 155326 463024, 155039 463024))" 
# )
###

zip_file = "example.zip"
gpkg_file = bgt_utils.import_to_geopackage(
    task = None,
    zip_file_name = zip_file,
    geopackage = "example.gpkg" )

# qgs.exitQgis()
