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
from enum import Enum, IntEnum
import wx
from .panelsbase import PanelTests_Base
from ..scriptartwork import ScriptArtwork
from ..forms.form_ontestfailure import FormOnTestFailure

class RunState(Enum):
    IDLE = 1
    RUN_SINGLE = 2
    RUNNING = 3
    PAUSED = 4
    FINISHED = 5
    DO_SETUP_FUNC = 6
    DO_CLEANUP_FUNC = 7
    WAIT_TEST_END = 8
    ERROR = 9
    START_FIRST = 10

class RunAction(Enum):
    NONE = 1
    STOP_ALL = 2
    PAUSE = 6

class TestIcon(IntEnum):
    FAIL = 0
    PASS = 1
    TODO = 2
    WARN = 3
    IDLE = 4
    RUNNING = 5
    PAUSED = 6

    @classmethod
    def GetImageList(cls):
        pass

class TestInfo:
    """ Structure to maintain information about a test.
    """

    def __init__(self, description, scriptname, **args):
        pass

class PanelTests(PanelTests_Base):
    """ Panel containing a treeview of all scripts in a given directory.
    """
    logger = logging.getLogger('happyscript')

    def __init__(self, parent, mngr: 'ScriptManager'):
        """ @param parent   Control to put this panel in.  Typically a notebook.
            @param mngr     The script manager
        """
        pass

    def init_list(self):
        """ Initialize the list with tests to execute.
        """
        pass

    def OnListSize(self, event):
        """ Adjust column width when form size changes.
        """
        pass

    def add_test(self, description, scriptname, **args):
        """ Add a single test to the test list.
            @param description    Name to appear in test list
            @param scriptname     dot-notation of test
            @param args           optional arguments to be given to test 
        """
        pass

    def get_tests(self, is_passed, include=None, exclude=None):
        """ Get list of tests that have passed or have not (yet) passed.
            
            @param is_passed  True to get list of passed tests, False for failed or not executed
            @param include    optional, list of test to include, other will be disregarded
            @param exclude    optional, list of tests to exclude
        """
        pass

    def OnBtnStartClick(self, event):
        pass

    def OnBtnPauseClick(self, event):
        pass

    def OnBtnStopClick(self, event):
        pass

    def reset_icons(self):
        """ Set all the icons right for a new test run
        """
        pass

    @property
    def state(self):
        pass

    @state.setter
    def state(self, value):
        """ Sets the next state for the test state machine.
            Activates timer such that state will be executed.
            Also checks some state changes to see if they are valid
        """
        pass

    def OnTmrStateMachine(self, event):
        pass