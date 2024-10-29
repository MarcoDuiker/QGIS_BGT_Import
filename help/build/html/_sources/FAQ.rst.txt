FAQ
***


Why did you make this plugin?
=============================

In my professional life I almost exclusively use Free an Open Source Software. I am very grateful that all those very nice products made by nice people are available to me free of charge and license hassles.

As Open Source is not about "taking", but much more about "giving" I like to do my share in giving. I try to spread knowledge by climbing the stage at almost all conferences I attend, by writing on eg. `QGIS.nl <http://www.qgis.nl/>`_, and by teaching at `Geo Academie <http://www.geo-academie.nl/>`_. 

My frustrations using the BGT in QGIS during teaching one of my courses led to this plugin. It is a completely volunteered effort, and I do not make any money out of it. Unfortunately the last incarnation of this plugin took a lot of time to create.

Why all those funnels next to the layer names in the table of contents?
=======================================================================

Those funnels indicate that there is a filter active on the layer. In this case all objects (features) which are expired (have a non-empty ``eindRegistratie`` ) are filtered out.



Why is the tab ("Import individual files") still in the plugin?
===============================================================

Actually, the stuff used to make the "Step 2: Convert" tab work is made with the "Import individual files" tab. I might have missed something. So, there you have a way to check the import done from the "Step 2: Convert" tab. If you find a mistake or something I missed, please `report the issue <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_.

Of course it is also handy if you need only one or two gml files from the BGT.

Beware: As the ``.gfs`` files used by the plugin are getting tweaked more and more using this "Import individual files" tab might give you inferior result compared to the "Step 2: Convert" tab. The "Import individual files" tab does not have support for non-linear geometries ("bogen") and does not support "voorloopnullen" on eg. BAG id's.



Why is the BGT-zip containing all those bloated gml files smaller than the geopackage containing the same data?
===============================================================================================================

The gml files contain objects, optionally having points, lines and polygons. To use them in QGIS these object needs to be split in up to 3 layers containing only lines, only points or only polygons. Of course all information shown in the attribute table is then duplicated or triplicated. And of course, zip is a very powerful way of making text files (much) smaller.

Furthermore spatial indexes are added which gives you the nice performance compared to using the gml files directly.


Your styling sucks! Can I apply my own default styling?
=======================================================

The styling mimics the 'official' styling of the BGT for a large part. It is rather complex, and I have made mistakes (please correct me where possible). But ... if I had done the styling myself, it would have looked much worse!

Anyhow, you can add your own default styling for a layer in the ``user_qml`` folder in the plugin folder. Naming convention will be obvious once you look at the files in the ``qml`` folder in the plugin folder.

In the plugin folder you will find several folders with useful symbols to use in your styling.

If you have created a nice styling, please share it!


I like to run a BGT download and import automagically on a regular basis. Can your plugin help?
===============================================================================================

The ``utils.py`` script in the ``bgt_utils`` folder in the plugin folder contains some functions which will help you.

I like this plugin. Can I buy you a beer?
=========================================

How nice of you to ask! I know a lot of people are using this plugin and as the Dutch geo-information scene is rather small I must bump into them quit a lot. It would be so nice to hear a kind word every now and again. 

So yes, please, thank you! 
But do remember, I don't like the sweet beers that much (I already am a very sweet person ;-)).



