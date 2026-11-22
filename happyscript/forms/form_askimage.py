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
from .formsbase import FormAskImage_Base

class FormAskImage(FormAskImage_Base):
    """ Form for asking something to operator
    """

    def __init__(self, message, filename, arrow_pos=None, yesno=False, cancel=False, numeric=False):
        """ @param parent   Control to put this panel in.  Typically a notebook.
            @param dirname  Directory name to reads scripts from.
        """
        pass

    def draw_arrow(self, bitmap, arrow_pos, scale=1.0):
        """ Draw an arrow to a point of interest.
            Arrow direction is adapted in case point is too close to right or bottom edge.
        """
        pass

    def OnButtonOK(self, event):
        pass

    def OnButtonNo(self, event):
        pass

    def OnButtonCancel(self, event):
        pass
if __name__ == '__main__':
    app = wx.App()
    form = FormAskImage('Dit is\n een test.', 'demo_pcb.jpg', (50, 600), yesno=False, cancel=True, numeric=True)
    form.ShowModal()
    app.MainLoop()