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
import os, configparser

class IniFileMeta(type):

class IniFile(metaclass=IniFileMeta):
    __configparser_object = None
    __filename = None

    @classmethod
    def read(cls, filename: str, /, generate_default: bool=True):
        """ Read values from the given ini-file.
            Only sections and values that are present as inner classes of this class will be read.
            If the file does not exist, it can be created with default values.

            :param filename: The name of the ini-file to read.
            :param generate_default: If True, the file will be created with default values if it does not exist.
        """
        pass

    @classmethod
    def dataclass_sections(cls):
        pass

    @classmethod
    def print_dataclass(cls):
        pass

    @classmethod
    def write(cls):
        """ Write the current values to the ini-file.
            Any changes to the file will be lost.
            TODO: 
        """
        pass

    @classmethod
    def get_section(cls, name: str):
        """ returns a configparser section for the given name, or an empty section if the name is not found.       
        """
        pass

    @classmethod
    def sections(cls):
        """ Returns a list of all sections in the ini file. """
        pass

    @classmethod
    def has_section(cls, section: str) -> bool:
        """ Checks if the given section exists in the ini file. """
        pass

    @classmethod
    def has_option(cls, section: str, option: str) -> bool:
        """ Checks if the given option exists in the given section of the ini file. """
        pass

    @classmethod
    def set(cls, section: str, option: str, value: str):
        """ Sets the value of the given option in the given section of the ini file. """
        pass