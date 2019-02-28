# -*- coding: utf-8 -*-

"""Cloud Chain Core main module."""

# DEBUG OPTION
_debug = True
_test = True

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
    if _debug:
        # display the debug main menu
        debugmainmenu.display()
    
