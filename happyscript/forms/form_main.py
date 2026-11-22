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
import wx
import wx.py as py
import sys, os, configparser, subprocess
try:
    from agw import aui
except ImportError:
    import wx.lib.agw.aui as aui
from ..scriptartwork import ScriptArtwork
from .form_ontestfailure import FormOnTestFailure
from .form_serials import FormSerials
from ..panels.panel_messages import PanelMessages
from ..panels.panel_tests import PanelTests
from ..panels.panel_log import PanelLog
from ..charts.panel_charts import PanelCharts
from .form_main_base import FormMain_Base

class FormMain(FormMain_Base):
    VALID_OPERATORS = ('OPERATOR', 'TECHNICIAN', 'ENGINEER', 'EXPERT')

    def __init__(self, script_manager):
        pass

    def BeforeShow(self):
        """ Method to be called before the form is first shown.
            The previous user selection and form layout will be restored.
        """
        pass

    def OnMnuLayoutClicked(self, event):
        pass

    def AddCustomPanel(self, title, panelType, **args):
        """ Add a custom panel to the pane with control panels.
            The panel constructor MUST have a parameter named 'parent'.  This will be filled in 
            automatically with the object containing the new panel. 
        
            @param  Title        Title for the panel
            @param  panelType    class to instantiate
            @param  args         parameters to supply to the constructor of the class
        """
        pass

    def HideCustomPanels(self):
        """ If there are no custom panels in the "ControlPanels" pane, hide that pane.
            This doesn't work properly if the pane has been docked together with another pane.
        """
        pass

    def SwitchUser(self, user):
        """ Switches the layout to the user "OPERATOR", "TECHNICIAN", "ENGINEER",= or "EXPERT".
            Layout for current user is saved to ini-file, and layout for new user
            is restored from ini-file.
            Different options are enabled/disabled depending on user level.
        """
        pass

    def RestorePosition(self):
        """ Restore the position of the window and the panes
        """
        pass

    def SavePosition(self, also_save_user=False):
        """ Save the position of the window and the panes
        """
        pass

    def OnFormClose(self, event):
        pass

    def TogglePanel(self, panel):
        pass

    def OnBtnScripts(self, event):
        pass

    def OnBtnPython(self, event):
        pass

    def OnBtnLogging(self, event):
        pass

    def OnBtnMessages(self, event):
        pass

    def OnBtnTestList(self, event):
        pass

    def OnBtnCharts(self, event):
        pass

    def OnBtnControls(self, event):
        pass

    def OnLayoutOperator(self, event):
        pass

    def OnLayoutTechnician(self, event):
        pass

    def OnLayoutEngineer(self, event):
        pass

    def OnLayoutExpert(self, event):
        pass

    def OnResetLayout(self, event):
        pass

    def OnBtnExit(self, event):
        pass

    def PushShellCommand(self, cmd):
        """ Push a command in the Python shell window.
        """
        pass

    def OnGuiTimer(self, event):
        pass

    def ClearLogs(self):
        """ Clears the logs in the message area and the log window.
        """
        pass

    def OnMnuSettingsClicked(self, event):
        pass

    def DisableSettingsButton(self):
        """ Disable the settings button in the toolbar.
            This is used when no ini file is set.
        """
        pass

    def OnBtnHelp(self, event):
        pass