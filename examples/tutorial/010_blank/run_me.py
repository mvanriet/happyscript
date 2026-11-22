
# We're deleting any old GUI settings file so that you start with a default state.
# This is just for this tutorial; you don't need to do this in your own programs.
import os
if os.path.exists("happyscript.ini"): os.remove("happyscript.ini")

#
# Tutorial 010: just create the script manager and run the GUI
#
# You can't really do anything with this, except for testing the different buttons
# in the GUI.
# Try pressing the 'User' button in the top-left.  More options are available when
# more 'advanced' users are selected.
#

import happyscript                                        # import the package
mngr = happyscript.ScriptManager()                        # instantiate script manager
mngr.run()                                                # start the GUI

