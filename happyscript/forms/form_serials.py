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
import re
import wx
from .formsbase import FormSerials_Base

class FormSerials(FormSerials_Base):
    """ Ask for up to 10 serial numbers.
        A label and match pattern can be given for each number.
        Result is a list of the serials, or None if user cancelled.
    """
    static_item = None

    @classmethod
    def show(cls, count, labels=None, filters=None):
        """ Instantiates the form (if necessary), then shows it.
        
            @param   count   how many numbers : 1 - 10 numbers
            @param   labels  List of strings to show left from each serial number entry field
            @param   filters regular expression for each serial number.  Items can be None
            @return  list of serial numbers, or None if no user cancelled
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

    def ask_serials(self, count, labels, filters):
        """ Called from class function show() to show the dialog.
            Initializes everything, shows the dialog, and then determines the result to return.
        """
        pass

    def handle_ontext(self, num):
        """ Checks serial numbers whenever the text in on of the text boxes changes.
            Color will be updated to green or red to indicate validity.
            'OK' button is enabled accordingly.
        """
        pass

    def OnText1(self, event):
        pass

    def OnText2(self, event):
        pass

    def OnText3(self, event):
        pass

    def OnText4(self, event):
        pass

    def OnText5(self, event):
        pass

    def OnText6(self, event):
        pass

    def OnText7(self, event):
        pass

    def OnText8(self, event):
        pass

    def OnText9(self, event):
        pass

    def OnText10(self, event):
        pass

    def handle_enter(self, num):
        """ Moves to next field upon pressing enter in a serial number text field.
        """
        pass

    def OnEnter1(self, event):
        pass

    def OnEnter2(self, event):
        pass

    def OnEnter3(self, event):
        pass

    def OnEnter4(self, event):
        pass

    def OnEnter5(self, event):
        pass

    def OnEnter6(self, event):
        pass

    def OnEnter7(self, event):
        pass

    def OnEnter8(self, event):
        pass

    def OnEnter9(self, event):
        pass

    def OnEnter10(self, event):
        pass

    def OnBtnCancel(self, event):
        pass

    def OnBtnOK(self, event):
        pass
if __name__ == '__main__':
    import wx
    app = wx.App()
    result = FormSerials.show(3, ['Logic Board', 'Power board', 'Micro ZED'], ['([0-9])\\w+', None, '([0-9])\\w+'])
    print(result)