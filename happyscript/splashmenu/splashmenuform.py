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
import os, sys, subprocess
from ..imglib import all_images

class ButtonInfo:
    """ Holds information about a button : the actual button object and the program and its arguments.
    """

    def __init__(self, button: wx.BitmapButton):
        pass

class SplashMenuForm(wx.Frame):

    def __init__(self, num_x, num_y, border, title):
        """ See constructor of SplashMenu for parameter details.
        """
        pass

    def DoExit(self, event):
        pass

    def SetButtonImage(self, btn, image_source: str | wx.Image):
        """ Set the image for an imagebutton.
            The image is automatically scaled to fit the size of the button.
            Normally, a filename is provided, but a wx.Image is used internally for the Exit button.
        """
        pass

    def set_button(self, x, y, image, program, arguments):
        """ Set info for the button.
        """
        pass

    def OnButton(self, event):
        """ Handles click event for buttons that have been set with a program to execute.
            Menu is hidden while the program runs, and restored afterwards.
        """
        pass