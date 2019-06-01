# -*- coding: utf-8 -*-
__package__ = "cloud-chain.cloudchain"
__version__ = "0.1.3"

# DEBUG OPTION
_debug = False
# DEBUG RUN LOOP
_run = True
# TEST OPTION
_test = False
# LAUNCH ELECTRON APP
_electron_app = False


# IMPORTS #
# python library imports
import os
import platform

# local core library classes and functions are imported via core.main
from core.main import *


if __name__ == "__main__":
    # TEST OPTION
    if _test:
        # run through the testing script
        if platform.system == "Windows":
            os.system("start py test.py")
        elif platform.system == "Darwin":
            os.system("python3 test.py")
    
    # DEBUG OPTION             
    elif _debug:
        # DEBUG RUN LOOP
        while _run:
            # display the debug main menu
            debugmainmenu.display()
    
    # LAUNCH ELECTRON APP
    elif _electron_app:
        # launch the electron front end ui
        os.system("npm start")
    
    # interactive shell
    elif _run:
        print(__package__, " version: ", __version__)
    # CLEAN SYSTEM EXIT 
    else:
        sys.exit()