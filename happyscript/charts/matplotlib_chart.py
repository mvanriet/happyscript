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
import logging
import wx
try:
    from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
    from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
    from matplotlib.figure import Figure
    import matplotlib.pyplot as plt
    HAVE_MATPLOTLIB = True
except ImportError:
    HAVE_MATPLOTLIB = False

class MatPlotLibChart(wx.Panel):

    def __init__(self, parent_control, name):
        """
        Constructor
        """
        pass

    @property
    def name(self):
        pass

    @property
    def figure(self) -> 'Figure':
        pass

    def configure(self, /, x_label=None, y_label=None, title=None, y_log=None, x_log=None, x_range=None, y_range=None):
        """
        """
        pass

    def update(self, /, antialiasing=False):
        """ Indicate that a chart should be updated. To be executed by a chart series when data is added.
            The internal 'dirty' flag is set.
            Also, the on_update callback function is called (if one is set).

            In a a chart panel, the callback function will set a flag to indicate that the chart must
            be updated.
        """
        pass

    def redraw(self):
        """ Redraw the chart.
            Updates of the charts are 'lazy' : they are not recalculated when data is added.
            The GUI calls this function to ask for the chart to be redrawn.
            The internal 'dirty' flag is cleared.
        """
        pass

    def clear(self):
        """ remove all series from the chart
        """
        pass

    def delete_series(self, name):
        pass

    def add_series(self, name):
        pass

    def get_series(self, name):
        pass

    def get_data_as_text(self):
        pass