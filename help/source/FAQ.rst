FAQ
***

Why did you make this plugin?
=============================

In my professional life I almost exclusively use Free an Open Source Software. I am very gratefull that all those very nice products made by nice people are available to me free of charge and license hassles.

As Open Source is not about "taking", but much more about "giving" I like to do my share in giving. I try to spread knowledge by climbing the stage at almost all conferences I attend, by writing on eg. `QGIS.nl <http://www.qgis.nl/>`_, and by teaching at `Geo Academie <http://www.geo-academie.nl/>`_. 

My frustrations using the BGT in QGIS during teachinh one of my courses led to this plugin. It is a completely volunteered effort, and I do not make any money out of it. Unfortonately the last incarnation of this plugin took a lot of time to create.


Why does the progress indicator move in such a weird way?
=========================================================

The BGT download website does not give any information on the size of the downloads. So in the best MS tradition the progress indicator jumps from 'almost half way' to 'just started' as often as needed to get the download in.

A bug in the great (but very new) task manager in QGIS makes this matter even worse as the last very small task (applying styling to the BGT) gets the last 33% of the progress bar. 


Why is the second tab ("Individual Files") still in the plugin?
===============================================================

Actually, the stuff used to make the first tab work is made with the second tab. I might have missed something. So, there you have a way to check the import doen form the first tab. If you find a mistake or something I missed, please `report the issue <https://github.com/MarcoDuiker/QGIS_BGT_Import/issues>`_.

Of course it is also handy if you need only one or two gml files from the BGT.


Why is the BGT-zip containing all those bloated gml files smaller than the geopackage containing the same data?
===============================================================================================================

The gml files contain objects, optionally having points, lines and polygons. To use them in QGIS these object needs to be split in up to 3 layers containing only lines, only points or only polygons. Of course all information shown in the attribute table is then duplicated or triplicated. And of course, zip is a very powerfull way of making text (much) smaller.

Furthermore spatial indexes are added which gives you the nice performance compared to using the gml files directly.


I like this plugin. Can I buy you a beer?
=========================================

How nice of you to ask! I know a lot of people are using this plugin and as the Dutch geo-information scene is rather small I must bump into them quit a lot. It would be so nice to hear a kind word every now and again. 

So yes, please, thank you! 
But do remember, I don't like the sweet beers that much (I already am a very sweet person ;-)).



