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
from .histogram_series import HistogramSeries
from .chart import Chart

class HistogramChart(Chart):

    def __init__(self, parent_control, name, binsize):
        pass

    def add_series(self, name: str) -> HistogramSeries:
        pass

    def do_add_series(self, name: str) -> HistogramSeries:
        """ Create a new series for this chart.
            Base class will add it to the list of series
        """
        pass

    def get_data_as_text(self) -> str:
        """ Returns the data of all series as text.
        """
        pass