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
import datetime, logging, threading
from .scriptexceptions import ScriptUserAbortException
from .scriptexceptions import ScriptRecursiveAbortException

class ScriptThreadRunner:
    """ Separate class for things related to running a script in a thread.
        Maintains a recursion counter to allow scripts calling one another, using a single thread.
    """
    logger = logging.getLogger('happyscript.scriptrunner')
    MARKER_LEVEL = 25

    def __init__(self, ctrl):
        pass

    def execute_script(self, script_name, script_func, argvalues):
        """ Executes a script function
        """
        pass

    def execute_threadfunc(self, script_name, script_func, argvalues):
        """
            Executes a script function
        
            @param script_name : name of the script, e.g. "demo.test_loop"
            @param script_func : the function to execute, as an object
            @param extra_params : dictionary of extra parameters that may be passed to the test function
        """
        pass

class ScriptParallelThread(threading.Thread):
    thread_counter = 0

    def __init__(self, ctrl, func, arg_list):
        pass

    def run(self):
        """ This will be executed when start() is called.
        """
        pass

class ScriptRunner:
    """ Class to allow easy running of scripts from code.
        
        Looks up the script function object in the ScriptReader class.
        Looks up the parameters in the ScriptParams class.
        Sets 'busy' flag for the ctrl object (in ScriptThreadRunner)
    """
    logger = logging.getLogger('happyscript.runner')

    def __init__(self, script_params, script_readers, script_control):
        pass

    @property
    def test_passed(self):
        pass

    @property
    def busy(self):
        pass

    def find_scriptfunct(self, script_name):
        """ Find the script function, based on the dotted script name with
            directory name, filename, function name.
            Returns the script function, or None if it is not found.
        """
        pass

    def run_script(self, script_name, **extra_params):
        """ Start a script given the directory group_name, filename and function name.
        """
        pass

    def do_parallel(self, func, parname, parvalues, **extra_params):
        """ Run a method in parallel, supplying different values to the given parameter.
        """
        pass