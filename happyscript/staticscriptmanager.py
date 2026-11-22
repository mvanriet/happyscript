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
import os, logging, time
import wx
from .forms.form_main import FormMain
from .panels.panel_scripts2 import PanelScripts2
from .scriptcontrol import ScriptControl
from .testlog.printredirect import PrintRedirect
from .scriptrunner import ScriptRunner
from .scriptparams import ScriptParams
from .scriptgui import ScriptGui
from .scriptinfo import ScriptInfo
from .forms.form_serials import FormSerials
from .testlog.global_log_handler import GlobalLogHandler
from .testlog.log_to_text import LogToText
from .modulereader import ModuleReader
from .inifile import IniFile
from .forms.form_settings import FormSettings

class StaticScriptManager(object):
    """ Main class for Happyscript that manages the GUI and entire script execution environment.

        When using a 'StaticScriptManager', your application can be compiled into a standalone executable,
        but then you cannot reload scripts dynamically in the treeview.  Typically you use
        [ScriptManager][happyscript.scriptmanager.ScriptManager] during development, and switch to
        'StaticScriptManager' for the standalone executable.
    """
    dialog = None
    logger = logging.getLogger('happyscript')
    __the_one_and_only_instance = None
    ini = IniFile

    def __init__(self, title=None, colors=None, use_yaml=False):
        """ Constructor

        Args:
            title (str): title for main window.
            colors (list): color scheme for test list :
                    0=green, 1=blue, 2=yellow, 3=grey, 4=orange, 5=darker blue 
            use_yaml (bool): whether to use YAML when writing an info file.  Standard is json.

        Attributes:
            on_batch_start (callable): Set this to your callback function for the start of a batch.  It must take no arguments.
            on_batch_end (callable): Set this to your callback function for the end of a batch.  It must take no arguments.
        """
        pass

    def on_log_timer(self):
        pass

    def set_logfiles(self, fname: str=None, fdir: str=None, use_temp: bool=False):
        """ Set the filenames for logging and for the info file.

        To be used in the on_batch_start callback to specify where the info of your batch
        test will be stored.  Use together with [close_logfiles()][happyscript.staticscriptmanager.StaticScriptManager.close_logfiles] in the 
        on_batch_end callback.
        
        Args:
            fname (str): filename for logging, without extension.  Default 'happyscript'
            fdir (str): directory name, either relative or absolute.  Default './log'
            use_temp (bool): use .tmp as extension for logfile.  Will be renamed by close_logfiles()  
        """
        pass

    def close_logfiles(self):
        """ Closes all previously selected logfiles (if any) and starts using default logfile names.

            This is typically called in the on_batch_end callback.

            If a 'tmp' extension was used for the logfile, this is the moment it will be renamed to .log.

            See also:                
                [set_logfiles()][happyscript.staticscriptmanager.StaticScriptManager.set_logfiles]
        """
        pass

    def stop_scripts(self):
        """ Sets flag to ask the running script (if any) to terminate.
            The script should use the 'ctrl' object to check this flag.
        """
        pass

    def clear_log(self):
        """ Clear the 'log' and 'messages' windows.
        """
        pass

    def add_object(self, objName: str, theObject):
        """ Add an object that can be used as parameter in the script functions.

        Args:
            objName (str): Name you want to give to this object.  This must be a valid Python variable name.
            theObject (any): The object to add, which can be accessed by the given name.
        """
        pass

    def add_objects(self, *args, **kwargs):
        """ Add one or more object that can be used as parameter in the script functions.

        Args:
            *args : List of objects to add.
            **kwargs : objects to add, with the name taken from the specified parameter name.
        """
        pass

    def add_module(self, module, group_name=None):
        """ Reads scripts from a python module.
            All files in the directory will be scanned for test functions.
            A new tab will be added in the 'scripts' panel, and 
            all the files and their test functions will be shown in a treeview.
            The __init__.py file in the module should have an import for all python files you want to include.

        Args:
            module (module): The python module containing the scripts to add.
            group_name (str): Name for this set of scripts. Module name will be used if not specified. 

        See Also:
            [add_scripts()][happyscript.scriptmanager.ScriptManager.add_scripts]
        """
        pass

    def add_scripts(self, script_dir, group_name=None):
        """ Reads scripts from a directory.
            All python files in the directory will be scanned for test functions.
            A new tab will be added in the 'scripts' panel, and 
            all the files and their test functions will be shown in a treeview.

            Note that this is not possible with StaticScriptManager. Use ScriptManager instead.

        Args:
            script_dir (str):   Full path to the directory with scripts
            group_name (str):  Name for this set of scripts.  Dirname will be used if not specified. 

        See Also:
            [add_module()][happyscript.staticscriptmanager.StaticScriptManager.add_module]
            
        """
        pass

    def add_test(self, description, scriptname, **args):
        """ Add a test to the test list.
        """
        pass

    def add_tests(self, testlist):
        """ Add several test at once.
            Teslist must contain tuples containing the description and the test name
        """
        pass

    @property
    def on_cmd_line(self):
        """ sets the callback function for commands entered in the log window
        """
        pass

    @on_cmd_line.setter
    def on_cmd_line(self, value):
        """ sets the callback function for commands entered in the log window
        """
        pass

    def ask_serials(self, count, labels=None, filters=None, add_to_info=True) -> list[str] | None:
        """ Show standard form for asking serial numbers.
            The serials will be (by default) filled in in info, clearing any previous serials.
        
        Args:
            count (int):   how many numbers : 1 - 5 numbers
            labels (list of str):  List of strings to show left from each serial number entry field
            filters (list of str): regular expression for each serial number.  Items can be None
            add_to_info (bool):   Whether to add the serials to the info object

        Returns:
            list of serial numbers, or None if the user pressed the 'Cancel' button
        """
        pass

    def add_custom_panel(self, title, panelType, **args):
        """ Add a custom panel to the pane with control panels.
            The panel constructor MUST have a parameter named 'parent'.  This will be filled in 
            automatically with the object containing the new panel. 
        
        Args:
            title (str):        Title for the panel
            panelType (type):   class to instantiate
            args:               parameters to supply to the constructor of the class

        Returns:
            The newly created panel
        """
        pass

    def show_settings(self):
        pass

    def run(self):
        """ Starts the application.
            Not to be confused with ScriptPanelRunner.run(), which is used to run a script.
        """
        pass