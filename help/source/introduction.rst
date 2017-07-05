Introduction
************

About
=====
This plug-in is developed by Marco Duiker from `MD-kwadraat <http://www.md-kwadraat.nl/>`_ .

The plug-in provides a way to directly import Dutch Basisregistratie Grootschalige Topografie (BGT) gml files and select the wanted feature types. GML-light is not supported.
This plug-in avoids the problems with the multiple feature types present in BGT gml files. 

How does the plug-in work?
=========================
The BGT gml files can contain objects which have multiple geometries, of different types. Eg. the bgt_kunstwerkdeel.gml can contain polygons, lines and points for the same type of objects (class).

The plug-in scans the file to see which geometry types are used and will generate ogr import definition file (.gfs) for each type of geometry. 

As a .gfs file needs to have the same name as the .gml file (except for the extension of course) the gml file will be copied or symlinked. The name of the copy will contain a _V, _L or _P extension to denote either polygons (_V), lines (_L) or points (_P).

Once these files are generated, QGIS will read the right geometry type on openening the file with one of the _V, _L or _P extensions. No need to use the BGT import plug-in for that.


How to import BGT gml files?
============================
First download a zip with some BGT gml files from the `BGT download site <https://www.pdok.nl/nl/producten/pdok-downloads/download-basisregistratie-grootschalige-topografie>`_. Download small areas or be prepared to wait when importing!

Unzip the package so you get a folder with .gml files and use the import tool to select one or more BGT gml files.

Choose the geometry types to import and click the OK button. If you choose only one geometry type, the import process will go quicker as the importer only scans the file until it has found the first geometry of the chosen type.

The plug-in will generate the described (above) copies and import definition files (.gfs). If you've checked the "add to project" check box the plug-in will add the files as layers to your project.

Scanning BGT files can be a time consuming process especially on platforms with low io speed. Please be patient.







