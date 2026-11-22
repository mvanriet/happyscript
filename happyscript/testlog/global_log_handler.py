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
import logging, traceback
import queue

class LogData:
    msg = ''
    levelno = 0
    levelname = '[?]'
    exc_info = None

class PanelFormatter(logging.Formatter):
    """ Composes a single string with log text to show to the user.
        Main use here is to expand the message if arguments were specified.
    """

    def __init__(self):
        pass

    def format(self, record):
        pass

class GlobalLogHandler(logging.StreamHandler):

    def __init__(self):
        pass

    def add_callback(self, func):
        """ Add a callback function to be called when something is logged.
            Callback function must accept a LogData structure as parameter.
        """
        pass

    def run_callbacks(self):
        """ Executes the callback functions for all the items in the queue.
            This must be called regularly from the GUI thread.
        """
        pass

    def emit(self, record):
        """ Called when something is logged.
            This is executed in the thread of the calling function.  Therefore we just always
            put the log on the queue, and the queue will be emptied regularly in the GUI thread.
        """
        pass

    def add_line_from_print(self, msg, level):
        """ Method to be used by the printredirect class to transfer a printed text
            to the global log handler.
        """
        pass