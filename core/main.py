# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.main"
__version__ = "0.1.3"

# IMPORTS #
# python library imports 
import os
import sys
import platform
import datetime
import shutil

# third party package imports
import requests

# CCC CONFIG
from core.config.main import CORE_CONFIG

# CCC SETUP
from core.setup.main import SETUP
from core.setup.main import getip
from core.setup.main import DIRNAME
from core.setup.main import CANPATH
from core.setup.main import DIRPATH
from core.setup.main import CHGDIR

# CCC WRITER
from core.writer.main import writer_help
from core.writer.main import FileObject
from core.writer.main import Write2file

# CCC LOGGER
from core.logger.main import CORE_LOGGER

# CCC PYTHOS 
from core.pythos.main import CORE_PYTHOS
from core.pythos.main import rfs
from core.pythos.main import rfsm
from core.pythos.main import rootfile_list_2

# CCC IPFS 
from core.ipfs.main import CORE_IPFS
from core.ipfs.main import IPFS_NODE
from core.ipfs.main import IPFS_API
from core.ipfs.main import IPFS_API_CONNECTION
from core.ipfs.main import PRINT_IPFS_DEBUG_INFO
from core.ipfs.main import LAUNCH_SP_IPFS_DAEMON
from core.ipfs.main import LAUNCH_IPFS_DAEMON

# CCC TERMINAL CLIENT 
from core.terminalclient.main import CORE_INTERFACE
from core.terminalclient.admin import isUserAdmin
from core.terminalclient.admin import runAsAdmin 

# CCC NETWORKING SERVER 
from core.network.server.http import HOST_LOCAL_HTTP_SERVER_WIN

# CCC NETWORKING CLIENT 
from core.network.client.main import connect_socket
from core.network.client.main import open_socket
from core.network.client.main import connect_to_node

class CORE:
    def __init__(self):
        self.__ipfs = CORE_IPFS
        self.__config = CORE_CONFIG
        self.__logger = CORE_LOGGER

def catch():
    x = input(">")

def node_server_debug_client():
    os.system("start py -i core/nodeserver/client.py")

def setupsequence():
    #os.system("start echo system")
    setupdata = SETUP()
    for i in range(0, len(setupdata)):
        print(setupdata[i])
    catch()

def pythos_dir_list():
    pydl = CORE_PYTHOS().DirectoryObjectsList()
    for i in range(0, len(pydl)):
        pydlstr = pydl[i]._pathname
        patharray = pydlstr.split('\\')
        del patharray[0]
        #print(patharray)
        for j in range(0, len(patharray)):
            if patharray[j] == ".git":
                break
            elif patharray[j] == "website":
                break
            elif patharray[j] == "node_modules":
                break
            elif patharray[j] == "core":
                for z in range(0, len(patharray)):
                    print("[" + "______" * z, patharray[z])
            print("[")
    catch()

#### MODULE HELP FUNCTIONS ####
def _help_writer():
    print(writer_help)
    catch()

#### DEBUG MENU ####
# TODO: menu class heirarchy  

### SUBMENUS ###
# submenu.setup
ccc_setup_menu_dict = {
    "setup sequence": setupsequence,
    'root file system list 2': rootfile_list_2,
    'directory info': rfsm,
    "pythos dir list": pythos_dir_list
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
    "IPFS Daemon": LAUNCH_IPFS_DAEMON,
    "IPFS Daemon SP": LAUNCH_SP_IPFS_DAEMON,
    "IPFS API CONNECTION": IPFS_API_CONNECTION
}
ipfsmenu = CORE_INTERFACE(ccc_ipfs_menu_dict, "IPFS Menu")

# submenu.help 
ccc_help_menu_dict = {
    "Writer": _help_writer
}
helpmenu = CORE_INTERFACE(ccc_help_menu_dict, "Help Menu")

### MAIN MENU ###
# menu.main
ccc_menu_dict = {
    "Setup": setupmenu.display,
    "Network": networkmenu.display,
    "IPFS": ipfsmenu.display,
    "Help": helpmenu.display
}
debugmainmenu = CORE_INTERFACE(ccc_menu_dict, "CloudChainCore")