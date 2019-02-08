# -*- coding: utf-8 -*-

"""core.main module."""

# IMPORTS #

# python library imports 
import os
import sys
import platform
import datetime
import shutil

# third party package imports
import requests

# core module classes and function imports
from core.ipfs.main import IPFS_API
from core.ipfs.main import IPFS_API_CONNECTION
from core.ipfs.main import PRINT_IPFS_DEBUG_INFO

from core.terminalclient.main import Interface


# Github Repositories 
gitrepo_go_ipfs = "https://github.com/ipfs/go-ipfs.git"
gitrepo_ripple = "https://github.com/ripple/rippled.git"
gitrepo_ripple_net_crawler = "https://github.com/ripple/rippled-network-crawler.git"



def node_server_debug_client():
    os.system("start py -i core/nodeserver/client.py")

def httpserver():
    os.system("start py -m http.server --bind 127.0.0.1")

def setupsequence():
    os.system("start echo system")

ccc_menu_dict = {
    "node-server debug client": node_server_debug_client,
    "http server": httpserver
}

ccc_setup_menu_dict = {
    "setup sequence": setupsequence
}
        
mainmenu = Interface(ccc_menu_dict, "CloudChainCore")
setupmenu = Interface(ccc_setup_menu_dict, "Setup Menu")