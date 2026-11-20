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
import logging, os, time
import json, dataclasses, datetime, base64

class CustomJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder to handle additional data types :
    - Datetime objects are converted to ISO format strings
    - Dataclass instances are converted to dictionaries
    - Binary data (bytes, bytearray) are converted to base64 encoded strings
    """

    def default(self, obj):
        pass

class ScriptInfo(object):
    """ Maintains test information and writes it to disk
    """
    logger = logging.getLogger('happyscript')

    def __init__(self, testlist, use_yaml: bool):
        """ Constructor
            @param testlist    object maintaining a list of all production tests
            @param use_yaml    Use yaml to write info file ?
        """
        pass

    def clear(self):
        """ Clears all information
        """
        pass

    def set_serials(self, serials):
        """ Set the serials from a given list.
            Any previously set serials will be deleted.
        """
        pass

    def add_serial(self, *serials):
        """ Add one or more serial numbers.
        """
        pass

    def set_filename(self, fname):
        """ Sets the filename to write the data to.
            Set to 'None" to prevent writing the data
        """
        pass

    def write_file(self, fname=None):
        """ Write all the information to a text file.
            If no filename is given, the filename specified with set_filename() will be used.
            If it is None, data will not be written.
        """
        pass

    def update_file(self, force=False):
        """ Writes the output file when there have been changes, and last update has been some time (2s).
            @param   force    Force writing the file, even if there were no changes
        """
        pass

    @property
    def serials(self):
        pass

    def get_passed_tests(self, include=None, exclude=None):
        """ Return a list of all production tests that passed.
            @param include    optional, list of test to include, other will be disregarded
            @param exclude    optional, list of tests to exclude
        """
        pass

    def get_failed_tests(self, include=None, exclude=None):
        """ Return a list of all production tests that failed or didn't execute.
            @param include    optional, list of test to include, other will be disregarded
            @param exclude    optional, list of tests to exclude
        """
        pass

    def add(self, objName, theObject):
        """ Add a a piece of information under the specified name.
            Is called when you assign a value to a non-existent property.
            File is written to disk from time to time.
        """
        pass