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

class Chart(wxplot.PlotCanvas):
    """ Base object for all charts.
        Derived chart has to implement :
        * do_redraw (optionally)
        * do_add_series
        * get_data_as_text
    """
    COLORS = (wx.Colour(68, 114, 196), wx.Colour(237, 125, 49), wx.Colour(165, 165, 165), wx.Colour(255, 193, 4), wx.Colour(91, 155, 213), wx.Colour(112, 173, 71), wx.Colour(38, 68, 120), wx.Colour(158, 72, 14), wx.Colour(99, 99, 99), wx.Colour(153, 115, 0), wx.Colour(37, 94, 145), wx.Colour(67, 104, 43), wx.Colour(105, 142, 208), wx.Colour(241, 151, 90), wx.Colour(183, 183, 183), wx.Colour(255, 205, 51), wx.Colour(124, 175, 221))

    def __init__(self, parent_control, name):
        """
        Constructor
        """
        pass

    def get_series_color(self):
        """ Get next color to use for a newly added series.
        """
        pass

    @property
    def name(self):
        pass

    def configure(self, /, x_label=None, y_label=None, title=None, y_log=None, x_log=None, x_range=None, y_range=None):
        """
            
        """
        pass

    @property
    def on_update(self):
        """ The callback function for when data is modified.
        """
        pass

    @on_update.setter
    def on_update(self, value):
        """ Set the callback function for when data is modified.
        """
        pass

    @property
    def dirty(self):
        """ Returns if the chart needs updating or not.
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

    def do_redraw(self):
        """ Is called when the chart must be redrawn.
            Standard implementation below.
            May be overridden for special kinds of charts.
        """
        pass

    def delete_series(self, name):
        """ Remove a series from a chart.
        """
        pass

    def add_series(self, name):
        """ Create a new series for this chart.
            First checks if name is valid, then calls do_add_series of derived class to create the series.
            Series is added as attribute to the chart itself.
        """
        pass

    def do_add_series(self, name):
        """ To be implemented by derived class.
        """
        pass

    def get_series(self, name):
        """ Return a series by name, or None if it doesn't exist
        """
        pass

    def get_data_as_text(self):
        """ Returns the data of all series as text.
            TO BE IMPLEMENTED FOR EACH CHART TYPE
            Data must be separated by a tab for easy Excel import
        """
        pass