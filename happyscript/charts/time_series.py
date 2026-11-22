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
import time
import wx
from wx.lib import plot as wxplot

class TimeSeries(object):

    def __init__(self, chart, name, color, start_time=None):
        """
        Constructor
        """
        pass

    @property
    def name(self):
        pass

    def add_value(self, value: float, t: float=None):
        """ Add a value for a time chart.
            Time is by default the actual time.  Any time as returned by time.time() can be used.
            The start time of creating the chart is subtracted from the time.
        """
        pass

    def add_values(self, value_time_list: list):
        """ Add a list of data points (for a time series graph)
            timevalue_time_list_value_points must be a list of tuples with value as first element
            and time as second element.
            As with add_value, the start time of creating the chart is subtracted from the time.
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