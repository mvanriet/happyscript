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
from .formsbase import FormAskChoice_Base

class FormAskChoice(FormAskChoice_Base):
    """ Form for asking the operator to select something from a list
    """

    def __init__(self, message, choices):
        """ constructor
        """
        pass

    def OnTestClick(self, event):
        pass

    def OnButtonOK(self, event):
        pass

    def OnButtonCancel(self, event):
        pass
if __name__ == '__main__':
    app = wx.App()
    form = FormAskChoice('Dit is een test van een hele lange zin.', ['Test1', 'Test2 ', 'Test 3', 'TEST 5'])
    form.ShowModal()
    print(form.result)
    app.MainLoop()