# -*- coding: utf-8 -*-
__package__ = "cloud-chain.test"
__version__ = "0.1.3"

# DEBUG OPTION
_debug = True

# IMPORTS #
# python library imports 
import os
import sys
import platform
import datetime
import shutil
import time
import unittest

# third party package imports
def import_test_ipfsapi():
    try:
        import ipfsapi
    except ModuleNotFoundError:
        os.system("pip install ipfsapi")
        import ipfsapi

def import_test_requests():
    try:
        import requests
    except ModuleNotFoundError:
        os.system("pip install requests")
        import requests

def import_test_grip():
    try:
        import grip
    except ModuleNotFoundError:
        os.system("pip install grip")
        import grip

def import_test_config():
    try:
        from core.config.main import CORE_CONFIG
    except ModuleNotFoundError:


def import_test_setup():
    try:
        from core.setup.main import SETUP
        from core.setup.main import getip
        from core.setup.main import DIRNAME
        from core.setup.main import CANPATH
        from core.setup.main import DIRPATH
        from core.setup.main import CHGDIR
    except ModuleNotFoundError:
        print("IMPORT ERROR SETUP")

def import_test_writer():
    try:
        from core.writer.main import writer_help
        from core.writer.main import FileObject
        from core.writer.main import Write2file
    except ModuleNotFoundError:
        print("IMPORT ERROR WRITER")

def import_test_logger():
    try:
        from core.logger.main import CORE_LOGGER
    except ModuleNotFoundError:
        print("IMPORT ERROR LOGGER")

def import_test_pythos():
    try:
        from core.pythos.main import CORE_PYTHOS
        from core.pythos.main import rfs
        from core.pythos.main import rfsm
        from core.pythos.main import rootfile_list_2
    except ModuleNotFoundError:
        print("IMPORT ERROR PYTHOS")

def import_test_ipfs():
    try:
        from core.ipfs.main import CORE_IPFS
        from core.ipfs.main import IPFS_NODE
        from core.ipfs.main import IPFS_API
        from core.ipfs.main import IPFS_API_CONNECTION
        from core.ipfs.main import PRINT_IPFS_DEBUG_INFO
        from core.ipfs.main import LAUNCH_SP_IPFS_DAEMON
        from core.ipfs.main import LAUNCH_IPFS_DAEMON
    except ModuleNotFoundError:
        print("IMPORT ERROR IPFS")

def import_test_terminalclient():
    try:
        from core.terminalclient.main import CORE_INTERFACE
        from core.terminalclient.admin import isUserAdmin
        from core.terminalclient.admin import runAsAdmin 
    except ModuleNotFoundError:
        print("IMPORT ERROR TERMINAL CLIENT")

def import_test_network_server():
    try:
        from core.network.server.http import HOST_LOCAL_HTTP_SERVER_WIN
    except ModuleNotFoundError:
        print("IMPORT ERROR NETWORK SERVER")

def import_test_network_client():
    try:
        from core.network.client.main import connect_socket
        from core.network.client.main import open_socket
        from core.network.client.main import connect_to_node
    except ModuleNotFoundError:
        print("IMPORT ERROR NETWORK CLIENT")


def import_test_ALL():
    import_test_grip()
    import_test_requests()
    import_test_ipfsapi()
    import_test_ipfs()
    import_test_config()
    import_test_logger()
    import_test_network_client()
    import_test_network_server()
    import_test_pythos()
    import_test_setup()
    import_test_terminalclient()
    import_test_writer()

# local core library classes and functions are imported via core.main
from core.main import *

def test_main_menu():
    debugmainmenu.display()

def test_setup_functions():
    s = SETUP()
    d = DIRNAME()
    dd = DIRPATH()
    print(s, d, dd)


def test_IPFS():
    # launch ipfs daemon
    try:
        LAUNCH_IPFS_DAEMON()
    except Exception as error:
        debug.log(error)
        return
    # 3 second delay to allow the daemon to start up
    for i in range(3):
        print(i)
        time.sleep(i)
    # IPFS API CONNECTION !!! ipfs daemon must be running
    try:
        ipfsnode = IPFS_API_CONNECTION()
    except Exception as error:
        debug.log(error)
        return
    
    # IPFS Debug variables from ipfsapi
    __ipfs_node_id = ipfsnode.id()
    __ipfs_bitswap_stat = ipfsnode.bitswap_stat()
    __ipfs_swarm_peers = ipfsnode.swarm_peers()
    __ipfs_swarm_addrs = ipfsnode.swarm_addrs()
    if _debug:
        PRINT_IPFS_DEBUG_INFO(__ipfs_node_id)
        PRINT_IPFS_DEBUG_INFO(__ipfs_bitswap_stat)
        PRINT_IPFS_DEBUG_INFO(__ipfs_swarm_peers)
        PRINT_IPFS_DEBUG_INFO(__ipfs_swarm_addrs)


def test_terminalClient():
    testdict = {"testMenuFunction": test_return}
    testUI = CORE_INTERFACE(testdict, "testTitle")
    testUI.display()

def test_return():
    return "test"

def test_ALL():
    import_test_ALL()
    test_IPFS()
    test_terminalClient()
    test_main_menu()
    test_setup_functions()

if __name__ == "__main__":
    test_ALL()