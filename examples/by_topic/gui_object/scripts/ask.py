
from happyscript import Gui


def a_simple_ask(gui: Gui):
    ''' @public
        Asks your name and says hello
    '''
    who = gui.ask("What is your name ?")
    print("Hello %s" % who)


def b_ask_with_default(gui: Gui):
    ''' @public
        Asks your name and says hello.
        Now a default value is provided.
    '''
    who = gui.ask("What is your name ?", default_value="John Doe")
    print("Hello %s" % who)


def c_handle_cancel(gui: Gui):
    ''' @public
        Asks your name and says hello.
        Handles the case when the user cancels the dialog.
    '''
    try:
        who = gui.ask("What is your name ?")
        print("Hello %s" % who)
    except ValueError:
        print("The user probably cancelled the dialog")
