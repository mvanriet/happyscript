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
import os, inspect, traceback
import wx
import importlib.util

class ScriptReader:
    """ Imports scripts from a single directory.
    """

    def __init__(self, script_dir, group_name=None):
        """
            @param runner   Reference to the ScriptRunner that instantiated this reader
            @param script_dir  Directory to load the scripts from
        """
        pass

    def reload(self):
        """ Reloads all scripts of this directory.
        """
        pass

    def read_single_file(self, filename):
        """ Import a python python file, and find all functions in it.
            A treeview item with the file name is created, and child nodes for each function.
            A reference is kept to all of the functions to call them later on.
        """
        pass

    def get_file_list(self):
        """ Get a list of all script files.
        """
        pass

    def get_func_names(self, filename):
        """ Get all the script functions in a script file.
            @param filename   Filename, as returned by get_file_list
        """
        pass

    def get_help(self, filename, funcname):
        pass

    def get_func(self, filename, funcname):
        pass