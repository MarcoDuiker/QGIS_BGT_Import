Introduction
************

About
=====
This plug-in is developed by Marco Duiker from `MD-kwadraat <http://www.md-kwadraat.nl/>`_ .

The plug-in provides a way to directly import Dutch Basisregistratie Grootschalige Topografie (BGT) data into QGIS, avoiding the (silent !) errors which occur using the standard QGIS import utilities. The phenomenon of the silent errors is explained on `QGIS.nl (in Dutch) <http://www.qgis.nl/2017/07/16/de-qgis-bgt-plugin/>`_.

Furthermore the plugin downloads the BGT data from map extent or intersect layer. On importing the data a nice styling mimicking the official one is added on the go. When adding the layers to the project, expired objects are filtered out.


How does the plug-in work?
==========================

You will find the plugin in the Vector menu.

The BGT gml files can contain objects which have multiple geometries, of different types. Eg. the bgt_kunstwerkdeel.gml can contain polygons, lines and points for the same type of objects (class).

The plug-in scans the file to see which geometry types are used and will generate ogr import definition file (.gfs) for each type of geometry. 

As a .gfs file needs to have the same name as the .gml file (except for the extension of course) the gml file will be copied or symlinked. The name of the copy will contain a _V, _L or _P extension to denote either polygons (_V), lines (_L) or points (_P).

Once these files are generated, QGIS will read the right geometry type on openening the file with one of the _V, _L or _P extensions. No need to use the BGT import plug-in for that.


How to import BGT gml files?
============================
First download a zip with some BGT gml files from the `BGT download site <https://www.pdok.nl/nl/producten/pdok-downloads/download-basisregistratie-grootschalige-topografie>`_. Download small areas or be prepared to wait when importing!

Unzip the package so you get a folder with .gml files and use the import tool to select one or more BGT gml files.

Choose the geometry types to import and click the OK button. If you choose only one geometry type, the import process will go quicker as the importer only scans the file until it has found the first geometry of the chosen type.

When importing large and/ or a lot of BGT gml files it is recommended to use the option to inspect a most a limited number of objects to find the requested geometry types. This wil speed up the import process a lot!

The plug-in will generate the described (above) copies and import definition files (.gfs). If you've checked the "add to project" check box the plug-in will add the files as layers to your project.

Scanning BGT files can be a time consuming process especially on platforms with low io speed. Please be patient.







