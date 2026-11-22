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
from .time_series import TimeSeries
from .chart import Chart

class TimeChart(Chart):
    start_time = None

    def add_series(self, name: str) -> TimeSeries:
        pass

    def do_add_series(self, name: str) -> TimeSeries:
        """ Create a new series for this chart.
            Base class will add it to the list of series
        """
        pass

    def get_data_as_text(self) -> str:
        """ Returns the data of all series as text.
        """
        pass

    def add_values(self, t=None, **values):
        """ Add values to different series at once that are on this chart.
        
            @param  t        optional, timestamp to use
            @param  values   values to set, using named parameters to specify the series name
        """
        pass