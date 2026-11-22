
import happyscript


############################################################################################################

if __name__ == "__main__":

    mngr = happyscript.ScriptManager()                         # instantiate script manager

    testlist = [ ("Power On",      "scripts.ctrl.b_loop_with_abort"),
                 ("Test PCB1",          "scripts.except_and_assert.exception_div_0"), 
                 ("Print label",     "scripts.toby_and_carol.use_toby_and_carol"),
                  ]
    mngr.add_tests( testlist )                                      # add a list of tests
    
    mngr.run()                                                 # start the GUI
