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
import logging
from .panelsbase import PanelLog_Base

class PanelLog(PanelLog_Base):
    """ Panel with logging of all output with print().
        Also contains a command line to give user commands.
    """

    def __init__(self, parent):
        """ @param parent   Control to put this panel in.  Typically a notebook.
            @param dirname  Directory name to reads scripts from.
        """
        pass

    def clear(self):
        """ Clear the output.
            Must be called from the GUI thread, not from a script thread.
        """
        pass

    def OnBtnClearLog(self, event):
        """ Clears all text in the log window.
        """
        pass

    def HandleLog(self, logdata):
        """ Show given log in the output window.    
            Called from the global log handler
        """
        pass

    def OnSelectLogLevel(self, event):
        pass

    def OnBtnStop(self, event):
        pass

    def OnBtnResume(self, event):
        pass

    def OnSetFocus(self, event):
        pass

    def OnCmdKeyUp(self, event):
        pass

    def OnCmdEnter(self, event):
        """ Send present string on the command line to callback function
        """
        pass