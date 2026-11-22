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
from .formsbase import FormStop_base

class FormStop(FormStop_base):
    """ Form for asking the operator to select something from a list
    """

    def __init__(self, message, mngr):
        """ constructor
        """
        pass

    def OnBtnStop(self, event):
        pass

    def update_message(self, msg):
        """ Update the message that is shown.
        """
        pass