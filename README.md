# QGIS BGT Import Plugin

This plugin imports the Dutch Basisregistratie Grootschalige Topografie (BGT) gml files into QGIS. Either by downloading and importing a complete package directly from the BGT download site or by selecting and importing individual BGT gml files. 

The use of this plugin prevents data loss which will occur when opening the gml files directly in QGIS.

You will find the plugin in the Vector menu.

More info in the [help](https://marcoduiker.github.io/QGIS_BGT_Import/help/build/html/index.html). 

Please refer to metadata.txt for source code repository and bug tracking.

# PostGIS BGT Importer

The [`bgt_utils` folder](bgt_utils) contains a command line tool written in Python to import a downloaded BGT zip file into PostGIS. This will prevent the data loss  which will occur when using eg. ogr2ogr to import.

This tool can be used like this:

```
BGT2PostGIS.py -d bgt -s testschema ./example.zip
```

# Automated BGT download and import

The [`bgt_utils` folder](bgt_utils) contains example code which can be used to write Python scripts which download the BGT from the BGT download site and convert to either geopackage or PostGIS. It is rather easy to extend this to other [dataformats which can be written by OGR](https://gdal.org/en/stable/drivers/vector/index.html) as well.
