# -*- coding: utf-8 -*-
__package__ = "cloud-chain.cloudchain_core"
__version__ = "0.1.3"

# DEBUG OPTION
_debug = False
_test = False
_electron_app = True

# IMPORTS #
# python library imports
import os
import platform
# local core library classes and functions are imported via core.main
from core.main import *


if __name__ == "__main__":
    if _test:
        # run through the testing script
        if platform.system == "Windows":
            os.system("start py test.py")
        elif platform.system == "Darwin":
            os.system("python3 test.py")             
    elif _debug:
        # display the debug main menu
        debugmainmenu.display()
    elif _electron_app:
        # launch the electron front end ui
        os.system("npm start")
    else:
        sys.exit()