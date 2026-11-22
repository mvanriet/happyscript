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
import os

class SplashMenu:

    def __init__(self, mainfilename, num_x, num_y, /, border=50, title='Menu'):
        """ Object for displaying a menu with image buttons to start other programs.

        Args:
            mainfilename (str): the __file__ of your main program
            num_x (int): number of buttons in the horizontal direction
            num_y (int): number of buttons in the vertical direction
            border (int): border in pixels to use all around the form
            title (str): title of the menu window
        """
        pass

    def set_button(self, x: int, y: int, image: str, program: str, arguments: str | list[str]=None):
        """ Configure a button with an image and a program to execute.

        The image should be a .png file.  It is resized to fit the button.

        The program can be a Python script or an executable file.  Arguments can be
        supplied as a string or a list of strings.  If the program is in another 
        directory, it will be made the current working directory when running the program.

        Args:
            x (int): horizontal position of the button, 1 = leftmost
            y (int): vertical position of the button, 1 = topmost
            image (str): filename of the image to show on the button
            program (str): python file or .exe to run
            arguments (str | list[str]): argument or list of arguments to supply to the program
        """
        pass

    def run(self):
        """ Show the menu.
            Will return when the 'Exit' button is pressed.
        """
        pass