Limitations
************

Openbareruimtelabel (punt)
==========================

In the gml file :code:`bgt_openbareruimtelabel.gml` some label objects have multiple positions, with multiple rotations to place the labels.

The GDAL/OGR library which is used to read data into QGIS and which is used by this plugin as well does not support. It uses only the last label position. So, each label object in the gml file will be available in the imported geopackage, but only one label position defined in the label object is imported. 

Missging label positions can be identified by looking at the 'hoek' field in the attribute tabel. This field is filled with values written like (2:30,45). This means to 2 rotations, one being 30 degrees, the other one being 45 degrees. You can find any number of rotations. Any number higher than 1 means that multiple label positions for that label object are available in the gml file. Only one is imported.

The style which is applied by the plugin uses the correct rotation value for placing the one label imported for that object in the map.
