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

class FormSerials_Base(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnText1(self, event):
        pass

    def OnEnter1(self, event):
        pass

    def OnText2(self, event):
        pass

    def OnEnter2(self, event):
        pass

    def OnText3(self, event):
        pass

    def OnEnter3(self, event):
        pass

    def OnText4(self, event):
        pass

    def OnEnter4(self, event):
        pass

    def OnText5(self, event):
        pass

    def OnEnter5(self, event):
        pass

    def OnText6(self, event):
        pass

    def OnEnter6(self, event):
        pass

    def OnText7(self, event):
        pass

    def OnEnter7(self, event):
        pass

    def OnText8(self, event):
        pass

    def OnEnter8(self, event):
        pass

    def OnText9(self, event):
        pass

    def OnEnter9(self, event):
        pass

    def OnText10(self, event):
        pass

    def OnEnter10(self, event):
        pass

    def OnBtnOK(self, event):
        pass

    def OnBtnCancel(self, event):
        pass

class FormAskImage_Base(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnButtonOK(self, event):
        pass

    def OnButtonNo(self, event):
        pass

    def OnButtonCancel(self, event):
        pass

class FormAskChoice_Base(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnButtonOK(self, event):
        pass

    def OnButtonCancel(self, event):
        pass

class FormOnTestFailure_Base(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnBtnRetry(self, event):
        pass

    def OnBtnSkip(self, event):
        pass

    def OnBtnStop(self, event):
        pass

class FormStop_base(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnBtnStop(self, event):
        pass

class FormSettings_Base(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnBtnApply(self, event):
        pass

    def OnBtnCancel(self, event):
        pass