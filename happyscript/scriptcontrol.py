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
import time
from .scriptexceptions import ScriptUserAbortException

class ScriptControl:
    """ object to allow flow control during script execution
    """

    def __init__(self):
        pass

    def ok(self) -> bool:
        """ To test if the script should stop.  ok() will return True until the 'stop' button 
            is pressed.  Exit your script loop when ok() returns False.
        """
        pass

    def check(self):
        """ This function will check if the 'stop' button is pressed.
            If it is, an exception is raised, which will stop the script, and the script will
            be considered to have failed.
            Typically you call this regularly in a loop, so the script can be stopped
            without having to write a lot of code for error handling.
        """
        pass

    def sleep(self, time_in_seconds: float):
        """ Sleeps for the specified number of seconds.
            When the stop button is pressed, an exception will be raised and the
            script will be stopped (almost) immediately.
        """
        pass

    def run(self, script_name: str, **argv):
        """ Execute a script from within another script.
            The script will be run in the same way as if it was started from the GUI.
            The script will run in the same thread as the calling script, so the calling
            script will be paused until the called script is finished.

            script_name is of the form "directory.file.function"

            You may pass arguments to the script using keyword arguments.  If the script
            needs additional parameters, ScriptManager will try to find these out by itself.
        """
        pass

    def do(self, script_name: str, **argv) -> str:
        """ Similar to run(), but doesn't throw an exception.  Instead, it returns the error
            message if an error occurs, or None if the script runs successfully.
        """
        pass

    def do_parallel(self, func: str, parname: str, parvalues: list, **extra_params) -> list[str]:
        """ excecute a function in parallel using different values for a given parameter
        """
        pass