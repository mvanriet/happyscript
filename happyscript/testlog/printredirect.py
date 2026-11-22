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
import sys
import logging

class PrintRedirect:
    """ Class to handle redirection of print() output.
        Output is send to callback functions.
        Output is also written to logfile.
        Note that when the print() statement is in a different thread, then the logging functions will
        also be called from that thread, and any further processing as well (e.g. in log and message panels).
    """
    _redir = None
    _reerr = None
    _old_redir = None

    def __init__(self, globalloghandler, level=None):
        """ Constructor.
            @param globalloghandler   The GlobalLogHandler object that puts all text on a queue for the GUI
            @param level              Default level.  Normally 'info', could be logging.ERROR for stderr
        """
        pass

    def write(self, txt):
        pass

    def flush(self):
        pass

    @classmethod
    def start_redirection(cls, handler):
        """ Starts redirecting text to the message area.
        """
        pass

    @classmethod
    def stop_redirection(cls):
        pass