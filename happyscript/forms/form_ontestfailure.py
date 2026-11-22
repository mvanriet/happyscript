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
from .formsbase import FormOnTestFailure_Base

class FormOnTestFailure(FormOnTestFailure_Base):
    """ Form asking what to do after failure
    """
    static_item = None

    @classmethod
    def show(cls, testname):
        """ Instantiates the form if necessary (done only once).
            then shows the dialog as a modal dialog.
            
            Returns wx.ID_RETRY, wx.ID_FORWARD or wx.ID_STOP
        """
        pass

    @classmethod
    def cleanup(cls):
        """ destroys form upon application end exit.
        """
        pass

    def __init__(self):
        """ @param parent   Control to put this panel in.  Typically a notebook.
            @param dirname  Directory name to reads scripts from.
        """
        pass

    def OnBtnRetry(self, event):
        pass

    def OnBtnSkip(self, event):
        pass

    def OnBtnStop(self, event):
        pass
if __name__ == '__main__':
    import wx
    app = wx.App()
    form = FormOnTestFailure(None)
    form.Show()
    app.MainLoop()