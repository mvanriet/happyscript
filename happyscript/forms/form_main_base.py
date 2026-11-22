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
import wx.xrc
import wx.aui
ID_BTN_TESTLIST = 6000
ID_BTN_MESSAGES = 6001
ID_BTN_LOGGING = 6002
ID_BTN_SCRIPTS = 6003
ID_BTN_PYTHON = 6004
ID_BTN_CONTROLS = 6005
ID_BTN_CHARTS = 6006
ID_BTN_HELP = 6007

class FormMain_Base(wx.Frame):

    def __init__(self, parent):
        pass

    def OnFormClose(self, event):
        pass

    def OnGuiTimer(self, event):
        pass

    def OnMnuLayoutClicked(self, event):
        pass

    def OnMnuSettingsClicked(self, event):
        pass

    def OnBtnTestList(self, event):
        pass

    def OnBtnMessages(self, event):
        pass

    def OnBtnLogging(self, event):
        pass

    def OnBtnScripts(self, event):
        pass

    def OnBtnPython(self, event):
        pass

    def OnBtnControls(self, event):
        pass

    def OnBtnCharts(self, event):
        pass

    def OnBtnHelp(self, event):
        pass

    def OnBtnExit(self, event):
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