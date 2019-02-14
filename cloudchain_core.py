# -*- coding: utf-8 -*-

"""Cloud Chain Core main module."""

# DEBUG OPTION
_debug = True

# IMPORTS #

# python library imports 
import os
import sys
import platform
import shutil
import datetime

# third party python imports
import ipfsapi
import requests

# local core library classes and functions are imported via core.main
from core.main import *


if __name__ == "__main__":
    # display the main menu 
    mainmenu.display()
    
