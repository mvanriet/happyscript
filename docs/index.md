# Welcome the documentation for Happyscript

Happyscript is a framework intended for running Python scripts against electronic hardware
and test equipment in an engineering or production environment.

It offers :

* tabbed GUI
* logging window with command line with history
* script selection from a treeview
* predefined test lists
* Python console with code completion
* basic charts
* easy GUI functions for user interaction
* easy panels with user controls
* .ini-file settings window

## Installation

Just use `pip install happyscript`.  This will also install wxpython, which is the only dependency.

Matplotlib can be used for charts, but you have to install this manually.  It is not added as dependency to keep the number of dependencies low.

## ScriptManager

The [ScriptManager][happyscript.scriptmanager.ScriptManager] object takes care of the GUI.  The minimal program is this :
``` py
import happyscript
mngr = happyscript.ScriptManager()
mngr.run()
```
This will give you a main window with a lot of options, depending on the type of user.  Click the leftmost icon in the menu bar to enable more options.

You can get an idea of the possibilities by looking at the tutorial on [github](https://github.com/mvanriet/happyscript/tree/main/examples/tutorial/).  Further information will be gradually added here on ReadTheDocs.

Since [ScriptManager][happyscript.scriptmanager.ScriptManager] loads its Python scripts dynamically, the resulting application cannot be converted to a static executable.  To allow this anyway, there is a variant [ScriptManager][happyscript.staticscriptmanager.StaticScriptManager] which is similar, but requires you to import the scripts explicitly, and therefore does not offer script reloads.


## Splashmenu

Sometimes the user needs a nice menu to select different things to test.

This is easy to implement using the [SplashMenu][happyscript.splashmenu.splashmenumain.SplashMenu] object.  This code will show buttons for two tests, and an 'exit' sign :
``` python
import happyscript
menu = happyscript.SplashMenu(__file__, 2, 2)
menu.set_button(1,1, "image1.png", "test1.py")
menu.set_button(2,1, "subdir/another_image.png", "subdir/another_test.exe", "COM1:" )
menu.run()
```

See the [examples](https://github.com/mvanriet/happyscript/tree/main/examples/splashmenu) for a demo.
