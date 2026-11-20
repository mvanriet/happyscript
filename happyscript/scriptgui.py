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
import threading
from .scriptexceptions import ScriptUserAbortException
from .forms.form_askimage import FormAskImage
from .forms.form_askchoice import FormAskChoice
from .forms.form_stop import FormStop
from .charts.histogram_chart import HistogramChart
from .charts.scatter_chart import ScatterChart
from .charts.time_chart import TimeChart
from .charts.matplotlib_chart import MatPlotLibChart
from .charts.chart import Chart

class ScriptGui:
    """ Object with various functions to interact with the user / operator.
    """

    def __init__(self, mngr):
        pass

    def ask(self, message: str, default_value: str='') -> str:
        """ Asks user feedback using a text field.
            User can press cancel, which will raise an exception.
            The given text is returned.
        """
        pass

    def ask_number(self, message: str, default_value: int=None) -> int:
        """ Ask user feedback using a numeric field.
            User can press cancel, which will raise an exception.
            The given number is returned.
        """
        pass

    def ask_yesno(self, message: str, cancel: bool=False) -> bool:
        """ Ask for user feedback using a yes/no question.
            Cancel button is optional.  It will raise an exception.
            Returns True for 'yes', False for 'no'.
        """
        pass

    def ask_image(self, message: str, filename: str, arrow_pos=None, yesno=False, cancel=False, numeric=False):
        """ Ask user feedback while showing a picture.
            Feedback could be a text, numeric value or yes/no.
            An arrow can be drawn on the image to point the user to something.
            The entire dialog and the image is automatically scaled to fit the screen.  No need to
            make the image in a certain resolution.
            A cancel button may be shown.  When pressed, an exception will be raised.
            
            @param message   Message for user.  Use 
 to make a multi-line message.
            @param filename  Path to filename of image to show.  JPG, PNG, GIF, BMP are supported.
            @param arrow_pos  Tuple containing pixel-coordinates for the array to point to.  None
                              if no arrow must be shown.
            @param yesno      Set True if it must be just a yes/no value
            @param cancel     Set True if a cancel button must be shown
            @param numeric    Set True if the value entered must be numeric
            
            @return    For yes/no : True if 'yes' is pressed, otherwise False
                       For text field : string value of text field
                       For numeric : floating point value
        """
        pass

    def ask_choice(self, message: str, choices: list, do_assert: bool=True) -> int:
        """ Ask user to select option from a list
            
            @param message   Message for user.  Use 
 to make a multi-line message.
            @param choices   List of strings to choose from
            @param do_assert Upon cancel, throw an assertion.  Otherwise returns -1.
            
            @return    Number of selected choice (first=0), or -1 upon cancel
        """
        pass

    def ask_open_file(self, message, wildcard):
        """ Ask user to select a file with a filedialog

            @param message  Message for user. Use 
 to make a multi-line message.
            @param wildcard Wildcard for file dialog, to select a specific type of file (e.g .zip files)

            @return     Pathname to the file selected, or None if cancelled
        """
        pass

    def show_stop_dialog(self, message=None):
        """ Shows a non-modal form that stays on top.
            It contains a button to stop the actively running script(s).
        """
        pass

    def close_stop_dialog(self):
        """ Closes the stop dialog, if any.
            Is always called automatically when a script ends.
        """
        pass

    def add_scatter_chart(self, name) -> ScatterChart:
        """ Adds a scatter chart to the main dialog.
        """
        pass

    def add_time_chart(self, name) -> TimeChart:
        """ Adds a time chart to the main dialog.
        """
        pass

    def add_histogram(self, name: str, binsize: float) -> HistogramChart:
        """ Adds a histogram chart to the main dialog.
        """
        pass

    def add_matplotlib(self, name: str) -> MatPlotLibChart:
        """ Adds a matplotlib chart
        """
        pass

    def get_chart(self, name: str) -> Chart:
        """ Returns an object representing a previously defined chart.
            @return   chart object, or None if given chart was not yet defined.
        """
        pass

    def delete_chart(self, name: str):
        """ Deletes the chart with the give name
        """
        pass