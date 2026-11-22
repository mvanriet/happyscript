# Demonstrating the gui methods

from random import randrange

def ask_name(gui):
    ''' @public
        Asks your name and says hello
    '''
    who = gui.ask("What is your name ?")
    print("Hello %s" % who)

def ask_number(gui):
    ''' @public
        Asks a number
    '''
    rnd = randrange(10)+1
    num = gui.ask_number("Give a number between 1 and 10")
    if num==rnd:
        print("[PASS] Good guess")
    else:
        print("[FAIL] Too bad, it wasn't %d but %d" % (num, rnd) )

def ask_yesno(gui):
    ''' @public
        Asks a yes/no question
    '''
    if gui.ask_yesno("Are you OK ?"):
        print("Good, I'm fine too.")
    else:
        print("Too bad.  Hope things get better soon.")

def ask_yesno_cancel(gui):
    ''' @public
        Asks a yes/no question with 'cancel' option.
        When 'cancel' is selected, an exception will be thrown.
    '''
    if gui.ask_yesno("Is the frontpanel LED showing a red color ?", cancel=True):
        print("[PASS] Error LED test OK.")
    else:
        print("[FAIL] Error LED not showing correct color.")
        
def ask_open_file(gui):
    ''' @public
        Asks to select a file.
    '''
    the_file = gui.ask_open_file("Select a zip-file", "*.zip")
    print("You selected : ", the_file)

        
def ask_image_text(gui):
    ''' @public
        Asks text together with image
    '''
    msg = "Enter the refdes of the given component,\nCancel if it is not mounted."
    refdes = gui.ask_image(msg, "demo_pcb.jpg", (320,417), cancel=True )
    print("Calibration circuit ref is %s" % refdes)
    
def ask_image_yesno(gui):
    ''' @public
        Asks yes or no together with image
    '''
    mounted = gui.ask_image("Is Q13 mounted ? You should see a small black little component with 3 legs.", "demo_pcb.jpg", (281,544), yesno=True )
    
    if mounted:
        print("[PASS] Q13 is mounted")
    else:
        print("[FAIL] Q13 is missing.")

def ask_image_numeric(gui):
    ''' @public
        Asks yes or no together with image
    '''
    count = gui.ask_image("How many solder holes are filled ?", "demo_pcb.jpg", (909,410), numeric=True )
    
    if count > 3:
        print("[FAIL] Too many solder holes are filled")

def ask_choice(gui):
    ''' @public
        Asks user to select choices from a list
    '''
    colors = [ "Red", "Blue", "Green", "Orange", "Yellow"]
    result = gui.ask_choice("What is your favourite color ?", colors )
    
    if result < 0:
        print("[FAIL] No color selected")
    else:
        print("I like %s too !" % colors[result])
