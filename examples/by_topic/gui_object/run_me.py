
#
# Possibilities of the 'gui' object.
#
# Activate the treeview window with scripts and try them out.
#

import happyscript                                        # import the package
mngr = happyscript.ScriptManager()                        # instantiate script manager
mngr.add_scripts("scripts")                               # load the dir with scripts
mngr.run()                                                # start the GUI

