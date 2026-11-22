
import sys
import happyscript


############################################################################################################

if __name__ == "__main__":

    mngr = happyscript.ScriptManager()                         # instantiate script manager

    # first part of testing is always the same
    testlist = [ ("Power On",      "scripts.ctrl.b_loop_with_abort") ]

    # then some tests for PCB 2
    if len(sys.argv)==2 and sys.argv[1]=="2":
        testlist.extend( [
            ("Test PCB2",          "scripts.except_and_assert.exception_div_0"), 
            ] )
        
    # or some tests for PCB 3
    elif len(sys.argv)==3 and sys.argv[1]=="3":
        testlist.extend( [
            ("Test PCB3",          "scripts.except_and_assert.exception_div_0"), 
            (sys.argv[2],          "scripts.except_and_assert.exception_div_0"), 
            ] )
        
    # finally some common tests at the end
    testlist.extend( [
        ("Print label",     "scripts.toby_and_carol.use_toby_and_carol"),
        ])
    
    mngr.add_tests( testlist )                                 # add the list of tests
    mngr.run()                                                 # start the GUI
