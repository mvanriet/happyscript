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
class UserPanelValue:

    def __init__(self, value_source, on_set=None, on_update=None):
        """initialiser method
        SmartInput objects are used to keep track of GUI input values

        Arguments:
            value_source -- GUI object to retreive self.value from

        Keyword Arguments:
            on_set -- callback to be run after self.set(), receives self.value as its first argument (default: {None})
        """
        pass

    def do_set(self, value=None):
        """ Event handler for the 'set' button.
            Can also be use to set the value and trigger the on_set callback.
        """
        pass

    @property
    def value(self):
        """ Gets the value of the GUI object.
        """
        pass

    @value.setter
    def value(self, value):
        """ Sets the value of the GUI object immediately.
            If an 'update' method is defined, it will be called.
        """
        pass

    def update(self):
        """ Calls the 'on_update' method if it was defined.
            This is typically used to update a label related to the GUI object.
        """
        pass