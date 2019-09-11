Limitations
***********

Downloads
=========

The BGT server from where the data is downloaded might be slow, down, or intermittently available. This means that downloads can fail or take very, very long. On larger downloads you are more likely to run into trouble.

Kadaster has launched an `alternative download site with beta status <https://download.pdok.io/lv/bgt/viewer/>`_, but a much better performance. It is recommended to download your BGT zip there and then import this zip using the plugin.

Pand (punt) (Huisnummers)
=========================

Sometimes the gml file of bgt_pand containes multiple labels with multiple rotations for a pand.

Only the first label and the first rotation is used.


Openbareruimtelabel (punt)
==========================

In the gml file :code:`bgt_openbareruimtelabel.gml` some label objects have multiple positions, with multiple rotations to place the labels.

The GDAL/OGR library which is used to read data into QGIS and which is used by this plugin as well does not support this. 

This problem is mitigated, ONLY WHEN YOU USE THE FIRST TAB (Complete Package), by duplicating the features in :code:`bgt_openbareruimtelabel.gml` so that the GDAL/OGR library can import this layer correctly. However, if you don't have the Python package lxml available to QGIS, this can take a long time.

If you use the second tab (individual files) or for some reason, the duplication of features fail, the import process will only import the last label position. So, each label object in the gml file will be available in the import, but only one label position defined in the label object is imported. 

Missing label positions can be identified by looking at the 'hoek' field in the attribute table. This field is filled with values written like (2:30,45). This means to 2 rotations, one being 30 degrees, the other one being 45 degrees. You can find any number of rotations. Any number higher than 1 means that multiple label positions for that label object are available in the gml file. Only one is imported.

The style which is applied by the plugin uses the correct rotation value for placing the one label imported for that object in the map.
