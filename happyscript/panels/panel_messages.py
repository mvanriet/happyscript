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
import datetime, logging
from .panelsbase import PanelMessages_Base

class PanelMessages(PanelMessages_Base):
    """ Panel with messages to display to test operator.
    """

    def __init__(self, parent):
        """ @param parent   Control to put this panel in.  Typically a notebook.
        """
        pass

    def clear(self):
        """ Clear all messages from the list.
        """
        pass

    def OnListSize(self, event):
        """ Adjust width of 'Message' column upon resizing the panel.
        """
        pass

    def HandleLogData(self, logdata):
        """ Handles logdata from the GlobalLogHandler.
            This is called by the 
        """
        pass

    def AddListEntry(self, result, msg, color=None):
        """ Adds a message to the list.
        
            @param result    tag for the 'result' column, e.g. PASS, FAIL
            @param msg       single-line text message
            @param color     optional, color (wx....) for text
        """
        pass

    def OnBtnClearList(self, event):
        pass

    def OnSelectLogLevel(self, event):
        pass