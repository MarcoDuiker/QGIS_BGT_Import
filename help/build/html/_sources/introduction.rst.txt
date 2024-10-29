Introduction
************

About
=====
This plug-in is developed by Marco Duiker from `MD-kwadraat <http://www.md-kwadraat.nl/>`_ .

The plug-in provides a way to directly import Dutch Basisregistratie Grootschalige Topografie (BGT) data into QGIS, avoiding the (silent !) errors which occur using the standard QGIS import utilities. The phenomenon of the silent errors is explained on `QGIS.nl (in Dutch) <http://www.qgis.nl/2017/07/16/de-qgis-bgt-plugin/>`_.

Furthermore the plugin downloads the BGT data from map extent or intersect layer. On importing the data a nice styling mimicking the official one is added on the go. When adding the layers to the project, expired objects are filtered out.


How does the plug-in work?
==========================

You will find the plugin in the Vector menu. A menu bar with a button is added to the QGIS interface as well. If you cannot find it, you can activate it in the same manner as all other menu bars.

Using the menu item BGT Import or pressing the BGT Import button on the toolbar will open a window with serveral tabs. The function of these tabs are explained below:


Step 1: Download
-----------------

On this tab a zip file containing BGT data can be downloaded from PDOK. The area can be selected by the map extent or a layer. Furthermore a selection of featuretypes can be made.

Alternatively you can use zip files which you can download from the `BGT download site <https://app.pdok.nl/lv/bgt/download-viewer/>`_.

Downloading will take place in the background. When the download is done, a notification will be given and the file name of the downloaded zip will be inserted on the tab "Step 2: Convert".

Step 2: Convert
---------------

On this tab a zip file containing BGT data can be converted to a geopackage based on a set predefined import rules. If necessary objects are split to polygon, line and point layers. 

If not there, the zip file used for creating this geopackage is stored next to the geopackage for reference.

Converting will take place in the background. When the converting is done, a notification will be given and the file name of the created geopackage will be inserted on the tab "Step 3: Add to project".

Step 3: Add to project
----------------------

On this tab all layers in a geopackage containg BGT data are added to your project in a layer group.

Filtering is applied to remove all objects which are expired (have a non-empty ``eindRegistratie`` ). Furthermore, layer order and styling is applied to mimic the official BGT styling where possible. 

It is possible to have the layergroup saved as a QGIS layer file for future use in other QGIS projects. 



Import individual files
----------------------------

On this tab you can select one or more BGT gml files to import. The plug-in scans the file and will determine the import rules on the go. These import rules are saved to a ``.gfs`` file.

As a ``.gfs`` file needs to have the same name as the ``.gml`` file (except for the extension of course) the gml file will be copied or symlinked. The name of the copy will contain a ``_V``, ``_L`` or ``_P`` extension to denote either polygons (_V), lines (_L) or points (_P).

Once these files are generated, QGIS will read the gml files properly on opening the file with one of the _V, _L or _P extensions. No need to use the BGT import plug-in for that.

Scanning BGT files and determining the import rules can be a time consuming process especially on platforms with low io speed. Please be patient, as this operation is not running as a background task.

Warning
~~~~~~~

As the ``.gfs`` files used by the plugin are getting tweaked more and more using this second tab might give you inferior result compared to the first tab. The conversion on this tab does not have support for non-linear geometries ("bogen") and does not support "voorloopnullen" on eg. BAG id's.


Usage Tips
==========

If you import data using the last tab of this plugin ('Import individual files'), you can still apply a nice style. The styles you can find in the ``qml`` folder in the plugin folder.

If you don't like the default styles this plugin applies, you can override these on a per layer basis by adding files to the ``user_qml`` folder in the plugin folder. Naming convention will be obvious once you look at the files in the ``qml`` folder in the plugin folder.


Troubleshooting
================

The BGT is a complex dataset to import into a GIS package. Things can go wrong. See the limitations in this help and the `issues list <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_. if you think something went wrong.

If you need to investigate an import which seems of, first use the last tab of this plugin ('Import individual files') WITHOUT SETTING A MAXIMUM NUMBER OF GEOMETRIES TO INSPECT to import this file without the predefined import rules. If the file then imports well, please report the issue on the `issues list <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_, and make the ``.gml`` file available.

If the import still seems to be wrong then check if the import is really wrong, are that there is a mistake in the data. Most of the time you can find out by inspecting an object in the ``.gml`` file, and the imported version of this object. If you then find out that the import is wrong, please report the issue on the `issues list <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_, and make the ``.gml`` file available.




