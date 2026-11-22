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
import re
import wx
from .formsbase import FormSettings_Base

class FormSettings(FormSettings_Base):

    @classmethod
    def show_modal(cls, parent, iniclass):
        pass

    def __init__(self, parent, iniclass):
        """ @param parent   Control to put this panel in.  Typically a notebook.
            @param iniclass Class that inherits from happyscript.IniFile, which contains the settings to display.
        """
        pass

    def show_fields(self):
        pass

    def OnBtnApply(self, event):
        pass

    def OnBtnCancel(self, event):
        pass

    def save_settings(self):
        """ Save the settings to the ini file.
            This is called when the user clicks the "Apply" button.
        """
        pass