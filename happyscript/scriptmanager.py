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
import os
from .panels.panel_scripts2 import PanelScripts2
from .scriptreader import ScriptReader
from .staticscriptmanager import StaticScriptManager

class ScriptManager(StaticScriptManager):
    """
    classdocs
    """

    def __init__(self, title: str=None, colors=None, use_yaml: bool=False):
        """
            Constructor
            
            @param  Optional title for main window.
            @param  Optional color scheme for test list.
                    0=green, 1=blue, 2=yellow, 3=grey, 4=orange, 5=darker blue 
        """
        pass

    def add_scripts(self, script_dir: str, group_name: str=None):
        """ Reads scripts from a directory. 
            Then adds a script treeview window with the scripts from the specified directory.
            @param script_dir   Full path to the directory with scripts
            @param group_name  Name for this set of scripts.  Dirname will be used if not specified. 
        """
        pass