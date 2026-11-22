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
import wx, os
from .imglib import all_images

class ScriptArtwork(wx.ArtProvider):
    baseDir = None
    overrides = {'wxART_QUIT': 'exit.png', 'settings': 'settings.png', 'user': 'user_female_32.png', 'python': 'python.png', 'scriptlist': 'ScriptList.png', 'messages': 'MessageList.png', 'logging': 'Logging.png', 'tests': 'TestList.png', 'charts': 'charts.png', 'help': 'help.png', 'test_fail': 'TestFail.png', 'test_pass': 'TestOK.png', 'test_todo': 'Dash.png', 'test_warning': 'TestWarning.png', 'test_idle': 'TestIdle.png', 'test_running': 'TestRunning.png', 'test_pause': 'TestPause.png', 'script_list': 'ScriptList.png', 'layout_DD': 'Layout_DD.png', 'user_operator': 'UserOperator.png', 'user_expert': 'UserExpert.png', 'user_engineer': 'UserEngineer.png', 'user_technician': 'UserTechnician.png', 'reset': 'reset.png', 'control_panel': 'controls.png', 'red_dot': 'red_dot.png', 'red_square': 'red_square.png', 'play': 'play.png', 'skip': 'skip.png', 'idle': 'idle.png', 'disable': 'disable.png'}

    @staticmethod
    def register():
        """ Registers the artwork provider to wx.ArtProvider.
            baseDir is used as a flag so that we only do this once    
        """
        pass

    def CreateBitmap(self, _id, client, size):
        """ Returns bitmap if the 'id' matches a filename present in the artwork directory.
            Otherwise returns none, so the next artwork provider will be called.
        """
        pass