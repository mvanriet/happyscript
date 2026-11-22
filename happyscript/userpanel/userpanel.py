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
from .userpanelvalue import UserPanelValue

class UserPanel(wx.Panel):
    """
    Public methods
    """

    def __init__(self, parent):
        """GUI builder for widgets to be used with happyscript

        Keyword Arguments:
            parent -- The window parent. This may be, and often is, None.
        """
        pass

    def add_box(self, title: str) -> None:
        """adds a box with a title to be used to contain the widgets

        Arguments:
            title: label for the box
        """
        pass

    def add_buttons(self, label, event, button_labels: list[str]) -> None:
        """adds a horizontal row of buttons, which trigger the button_event(button_label) callback)

        Arguments:
            label: label to be placed left of the buttons, or None to have no label
            event: callback triggered on button presses
            button_labels -- list of labels (one for each button)
        """
        pass

    def add_slider(self, label: str, event, value: int, min_val: int, max_val: int) -> UserPanelValue:
        """ Adds a slider for the user to set a value.
        event function is called when the 'set' button is pressed, with the slider value as parameter

        Arguments:
            label: label to be placed left of the slider
            event: callback triggered when pressing the 'set' button
            value: slider initial value
            min_val: slider minimum value
            max_val: slider maximum value 

        Returns: object to access the slider value
        """
        pass

    def add_combo_box(self, label: str, event, choices: list[str]) -> UserPanelValue:
        """ Adds a combo box for the user to set a value.
        event function is called when the 'set' button is pressed, with the combo box value as parameter

        Arguments:
            label: label to be placed left of the combo box
            event: callback triggered when pressing the 'set' button
            choices: list of options to be presented in the combo box

        Returns: object to access the combo box value
        """
        pass

    def add_spin_control(self, label: str, event, value: int, min_val: int, max_val: int):
        """  Adds a spin control for the user to set a value.
        event function is called when the 'set' button is pressed, with the spin control value as parameter.

        Arguments:
            label: label to be placed left of the spin control
            event: callback triggered when pressing the 'set' button
            value: spin control initial value
            min_val: spin control minimum value
            max_val: spin control maximum value

        Returns: object to access the spin control value
        """
        pass

    def add_timer_control(self, label, event, interval_s):
        """ allows the user to periodically trigger a callback
            the timer interval is set with a spin control, in seconds
            pressing start or stop will (re)start or stop the interval timer

        Arguments:
            label -- label to be placed on the left
            event -- callback to be triggered each interval
            interval_s -- interval default value
        """
        pass
    '\n    private methods\n    '