
import happyscript

# create the menu
# first parameter must always be __file__; its location is used as base directory
# 2nd and 3rd are number of buttons in x and y direction
# 4th optional parameter = margin in pixels to take around the screen; default=50
menu = happyscript.SplashMenu(__file__, 2, 2, title="Demonstration of the splash menu")

# test script in the current directory
menu.set_button(1,1, "PCB1.png", "test_pcb1.py")

# test script in another directory, with a parameter
# the script will be run from 'subdir'
menu.set_button(2,1, "subdir/PCB2.png", "subdir/test_PCB2_3.py", 2 )

# test script in another directory, with two parameters
menu.set_button(1,2, "./subdir/PCB3.png", "subdir/test_pcb2_3.py", [3, "Heraeus"] )

# show the menu
menu.run()
