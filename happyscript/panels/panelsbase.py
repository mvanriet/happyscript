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

class PanelScripts_Base(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 477), style=0, name=wx.EmptyString):
        pass

    def btn_stopOnButtonClick(self, event):
        pass

    def OnBtnReload(self, event):
        pass

    def OnTreeLeftDoubleClick(self, event):
        pass

    def OnTreeKeyDown(self, event):
        pass

    def OnTreeSelChanged(self, event):
        pass

    def m_splitter2OnIdle(self, event):
        pass

class PanelMessages_Base(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 562), style=0, name=wx.EmptyString):
        pass

    def OnBtnClearList(self, event):
        pass

    def OnSelectLogLevel(self, event):
        pass

    def OnListSize(self, event):
        pass

class PanelLog_Base(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(783, 466), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        pass

    def OnBtnClearLog(self, event):
        pass

    def OnBtnStop(self, event):
        pass

    def OnBtnResume(self, event):
        pass

    def OnSelectLogLevel(self, event):
        pass

    def OnCmdKeyUp(self, event):
        pass

    def OnSetFocus(self, event):
        pass

    def OnCmdEnter(self, event):
        pass

class PanelTests_Base(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=0, name=wx.EmptyString):
        pass

    def OnBtnStartClick(self, event):
        pass

    def OnBtnPauseClick(self, event):
        pass

    def OnBtnStopClick(self, event):
        pass

    def OnListRightClick(self, event):
        pass

    def OnListSize(self, event):
        pass

    def OnTmrStateMachine(self, event):
        pass

    def OnMenuRun(self, event):
        pass

    def OnMenuEnable(self, event):
        pass

    def OnMenudisable(self, event):
        pass

    def OnMenuSkip(self, event):
        pass

    def OnMenuBreakpoint(self, event):
        pass

class PanelCharts_Base(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        pass

    def BtnCopyDataClick(self, event):
        pass

    def OnMakePretty(self, event):
        pass

    def OnBtnSaveBitmap(self, event):
        pass

    def OnRadioBoxMouseMode(self, event):
        pass

    def OnTimerAnimate(self, event):
        pass

    def OnRedrawTimer(self, event):
        pass

class PlotDialog(wx.Dialog):

    def __init__(self, parent):
        pass

    def OnClose(self, event):
        pass