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
import os
import logging
from ..panels.panelsbase import PanelCharts_Base
from ..charts.scatter_chart import ScatterChart
from ..charts.time_chart import TimeChart
from ..charts.histogram_chart import HistogramChart
from ..charts.matplotlib_chart import MatPlotLibChart

class PanelCharts(PanelCharts_Base):
    """ Panel containing one or more plots
    """

    def __init__(self, parent):
        """ @param parent   Control to put this panel in.  Typically a notebook.
            @param dirname  Directory name to reads scripts from.
        """
        pass

    def update(self):
        """ Triggers update of chart.
            The chart is not updated immediately, but using a 50ms timer.
            Note that we don't use a one-shot timer because that cannot be started from another thread.
        """
        pass

    def OnRedrawTimer(self, event):
        """ Charts are redrawn using a timer when necessary.
            This way, high-frequency updates of the chart will only be shown at a moderate rate.
            @TODO:   Update only visible chart
        """
        pass

    def OnRadioBoxMouseMode(self, event):
        pass

    def BtnCopyDataClick(self, event):
        pass

    def OnMakePretty(self, event):
        pass

    def OnBtnSaveBitmap(self, event):
        pass

    def get_chart(self, name):
        """ Returns chart object with the given name, or None if chart does not exist.
        """
        pass

    def delete_chart(self, name):
        """ Deletes the chart with the given name
        """
        pass

    def add_scatter_chart(self, name):
        """ Creates a new chart with the given options.
        """
        pass

    def add_time_chart(self, name):
        """ Creates a new time chart with the given options.
        """
        pass

    def add_histogram(self, name, binsize):
        """ Creates a new histogram chart with the given options.
        """
        pass

    def add_matplotlib(self, name):
        """ Creates a new matplotlib chart
        """
        pass

class PlotDialog(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnClose(self, event):
        pass
if __name__ == '__main__':
    app = wx.App()
    form = PlotDialog(None)
    form.ShowModal()
    app.MainLoop()