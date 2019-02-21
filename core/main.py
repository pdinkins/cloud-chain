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
from core.config.main import CORE_CONFIG

from core.logger.main import CORE_LOGGER

from core.ipfs.main import CORE_IPFS
from core.ipfs.main import IPFS_API
from core.ipfs.main import IPFS_API_CONNECTION
from core.ipfs.main import PRINT_IPFS_DEBUG_INFO
from core.ipfs.main import LAUNCH_SP_IPFS_DAEMON
from core.ipfs.main import LAUNCH_IPFS_DAEMON

from core.terminalclient.main import CORE_INTERFACE

from core.network.server.http import HOST_LOCAL_HTTP_SERVER_WIN

class CORE:
    def __init__(self):
        self.__ipfs = CORE_IPFS
        self.__config = CORE_CONFIG
        self.__logger = CORE_LOGGER

def node_server_debug_client():
    os.system("start py -i core/nodeserver/client.py")

def setupsequence():
    os.system("start echo system")

### SUBMENUS ###
# submenu.setup
ccc_setup_menu_dict = {
    "setup sequence": setupsequence
}
setupmenu = CORE_INTERFACE(ccc_setup_menu_dict, "Setup Menu")

# submenu.network
ccc_network_menu_dict = {
    "HTTP Server" : HOST_LOCAL_HTTP_SERVER_WIN,
    "node-server debug client": node_server_debug_client
}
networkmenu = CORE_INTERFACE(ccc_network_menu_dict, "Network Menu")

# submenu.ipfs
ccc_ipfs_menu_dict = {
    "IPFS Daemon": LAUNCH_IPFS_DAEMON
}
ipfsmenu = CORE_INTERFACE(ccc_ipfs_menu_dict, "IPFS Menu")

### MAIN MENU ###
# menu.main
ccc_menu_dict = {
    "Setup": setupmenu.display,
    "Network": networkmenu.display
}
mainmenu = CORE_INTERFACE(ccc_menu_dict, "CloudChainCore")