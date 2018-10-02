# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BGTImport
                                 A QGIS plugin
 Import Basisregistratie Grootschalige Topografie (BGT)
                             -------------------
        begin                : 2017-06-28
        copyright            : (C) 2017 by Marco Duiker - MD-kwadraat
        email                : md@md-kwadraat.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BGTImport class from file BGTImport.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bgt_import import BGTImport
    return BGTImport(iface)
