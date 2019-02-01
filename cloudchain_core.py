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

# local module imports
from core.terminalclient.main import *

# main script sequence that spawns subsequent processes decribed below
    
    # Establish setup sequence
    # User login sequence 


def node_server_debug_client():
    os.system("start py -i core/nodeserver/client.py")

def httpserver():
    os.system("start py -m http.server --bind 127.0.0.1")


ccc_menu_dict = {
    "node-server debug client": node_server_debug_client,
    "http server": httpserver
}

ui = Interface(ccc_menu_dict, "CloudChainCore")
ui.display()