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
from .panelsbase import PanelScripts_Base

class PanelScripts2(PanelScripts_Base):
    """ Panel containing a treeview of all scripts in a given directory.
    """

    def __init__(self, parent, script_reader, script_control):
        """ @param parent         Control to put this panel in.  Typically a notebook.
            @param script_reader  ScriptReader object that read all the scripts in the script dir.
            @param script_control  Object run scripts
        """
        pass

    def load_treeview(self):
        """ Load script names into the treeview.
        """
        pass

    def OnBtnReload(self, event):
        """ Reloads all scripts of this directory.
        """
        pass

    def OnTreeLeftDoubleClick(self, event):
        """ Double-click on an item in the treeview.
            If it is a treeview node of the function it is executed.
            (Treeview nodes of a file have the root as parent, all others are functions.)
        """
        pass

    def OnTreeKeyDown(self, event):
        """ Enter is pressed on an item in the treeview.
        """
        pass

    def ExecuteScriptForItem(self, item):
        """ Execute a script of a treeview item.
            This is called either upon double-clicking on an item, or pressing ENTER.
        """
        pass

    def OnTreeSelChanged(self, event):
        """ Update the description of the function when the selection in the treeview changes.
        """
        pass

    def btn_stopOnButtonClick(self, event):
        """ Use ScriptControl to stop any running in an orderly fashion. 
        """
        pass