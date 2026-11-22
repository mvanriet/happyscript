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
    """ A subclass of StaticScriptManager that allows live reloading of test scripts.
    """

    def __init__(self, title: str=None, colors=None, use_yaml: bool=False):
        """ Constructor

        Args:
            title (str): title for main window.
            colors (list): color scheme for test list :
                    0=green, 1=blue, 2=yellow, 3=grey, 4=orange, 5=darker blue 
            use_yaml (bool): whether to use YAML when writing an info file.  Standard is json.

        """
        pass

    def add_scripts(self, script_dir: str, group_name: str=None):
        """ Reads scripts from a directory.
            All python files in the directory will be scanned for test functions.
            A new tab will be added in the 'scripts' panel, and 
            all the files and their test functions will be shown in a treeview.

        Args:
            script_dir (str):   Full path to the directory with scripts
            group_name (str):  Name for this set of scripts.  Dirname will be used if not specified. 
        """
        pass