#=============================================================================================
# HAPPYSCRIPT - GUI framework for running python scripts in a test or production environment.
# Copyright (C) 2020  -  GNU GPL v3  -  Dekimo Products  -  www.dekimo.com
#
# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details : https://www.gnu.org/licenses/.
#=============================================================================================
import wx
from wx.lib import plot as wxplot

class ScatterSeries(object):

    def __init__(self, chart, name, color):
        """
        Constructor
        """
        pass

    @property
    def name(self):
        pass

    def add_point(self, x: float, y: float):
        """ Add a data point (for a scatter graph)
        """
        pass

    def add_points(self, xypoints: list):
        """ Add a list of data points (for a scatter graph)
            xypoints must be a list of tuples (x, y)
        """
        pass

    def clear(self):
        """ Clear the data points.
        """
        pass

    def get_points(self):
        """ Returns all the data points.
        """
        pass