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
import logging
import time
import os

class LogToText(object):
    """ Writes logs to a text file.
    
        Flush() is called regularly so that output is not lost if the program crashes.
    """

    def __init__(self):
        """
        Constructor
        """
        pass

    def set_filename(self, filename, /, use_temp=False):
        """ Sets the file name for log output.
            If the file already exists, output is appended.
            If it doesn't exist, it is created.
            If a directory name is used, it must exist.
        """
        pass

    def open(self):
        """ Opens the log file if necessary.
        """
        pass

    def close(self):
        """ Closes the logfile (if necessary).
            Trailing XML data will be written to complete the document.
        """
        pass

    def handle_log(self, logdata):
        """ Process log entry.
        """
        pass