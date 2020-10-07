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


First Tab: Complete package
---------------------------

**As PDOK has a new API which is not supported (yet) downloading straight from the plugin is not possible anymore.**

Alternatively you can use zip files which you can download from the `BGT download site <https://app.pdok.nl/lv/bgt/download-viewer/>`_.

Then based on a set of predefined import rules, the data is imported to a geopackage. If necessary objects are split to polygon, line and point layers. Then all layers are added to your project in a layer group. Filtering is applied to remove all objects which are expired (have a non-empty ``eindRegistratie`` ). Furthermore, styling is applied to mimic the official BGT styling where possible. 

The zip file which was downloaded is stored next to the geopackage for reference. Furthermore the layergroup is saved as a QGIS layer file for future use in other QGIS projects. 

Importing actions from this tab is done as a background task. The progress indicator in the status bar will show progress. During download this progress indicator will run to about 30% and the start at about 5% again. This is normal behavior. As long as the percentages are changing your download is running as it should. If you download large areas, be prepared to wait (a long time). And if you get bored you can always abort the download via the progress indicator.


Second Tab: Individual files
----------------------------

On this tab you can select one or more BGT gml files to import. The plug-in scans the file and will determine the import rules on the go. These import rules are saved to a ``.gfs`` file.

As a ``.gfs`` file needs to have the same name as the ``.gml`` file (except for the extension of course) the gml file will be copied or symlinked. The name of the copy will contain a ``_V``, ``_L`` or ``_P`` extension to denote either polygons (_V), lines (_L) or points (_P).

Once these files are generated, QGIS will read the gml files properly on opening the file with one of the _V, _L or _P extensions. No need to use the BGT import plug-in for that.

Scanning BGT files and determining the import rules can be a time consuming process especially on platforms with low io speed. Please be patient, as this operation is not running as a background task.

Warning
~~~~~~~

As the ``.gfs`` files used by the plugin are getting tweaked more and more using this second tab might give you inferior result compared to the first tab. The second tab does not have support for non-linear geometries ("bogen") and does not support "voorloopnullen" on eg. BAG id's.


Usage Tips
==========

If you import data using the second tab of this plugin ('Individual files'), you can still apply a nice style. The styles you can find in the ``qml`` folder in the plugin folder.

If you don't like the default styles this plugin applies, you can override these on a per layer basis by adding files to the ``user_qml`` folder in the plugin folder. Naming convention will be obvious once you look at the files in the ``qml`` folder in the plugin folder.


Troubleshooting
================

The BGT is a complex dataset to import into a GIS package. Things can go wrong. See the limitations in this help and the `issues list <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_. if you think something went wrong.

If you need to investigate an import which seems of, first use the second tab of this plugin ('Individual files') WITHOUT SETTING A MAXIMUM NUMBER OF GEOMETRIES TO INSPECT to import this file without the predefined import rules. If the file then imports well, please report the issue on the `issues list <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_, and make the ``.gml`` file available.

If the import still seems to be wrong then check if the import is really wrong, are that there is a mistake in the data. Most of the time you can find out by inspecting an object in the ``.gml`` file, and the imported version of this object. If you then find out that the import is wrong, please report the issue on the `issues list <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_, and make the ``.gml`` file available.




