# -*- coding: utf-8 -*-

"""Main module."""

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

# main script sequence that spawns subsequent processes decribed below
    
    # Establish setup sequence
    # User login sequence 

mainmenu.display()
