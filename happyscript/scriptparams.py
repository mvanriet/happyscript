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
import inspect
from .scriptexceptions import ScriptUserAbortException

class ScriptParams(object):
    """ Maintains a collection of objects that can be provided as parameter to script functions.
    """

    def __init__(self, ask_gui=None):
        """ Constructor
            @param ask_gui    Object with functions for asking a parameter if it is specified in the comments.
        """
        pass

    def add_object(self, objName, theObject):
        """ Add an object that can be used as parameter in the script functions.
        """
        pass

    def add_objects(self, *args, **kwargs):
        """ Add a number of objects.
            The name is derived from the keyword when using keyword arguments.
            When not using keyword arguments, the name is derived from a member  '__name__' that must be
            present for the object.  This is a convention, so this member must be explicitly added.
        """
        pass

    def get_param(self, param_name):
        """ Get value of a parameter.
        """
        pass

    def get_parameters(self, scriptObject, extraParams=None):
        """ Investigates which parameters a function needs, and returns a list of values for these parameters.
            Parameter names should match the names of objects added to the script manager.
            Additional parameters can be provided; they will override any existing objects with the same name
            (except for the reserved names 'mngr', 'ctrl', 'gui', 'info' which are always taken from the script manager).
        
            @param scriptObject : the function to analyze, as an object
            @param extraParams : dictionary of extra parameters that may be passed to the test function
        """
        pass