# -*- coding: utf-8 -*-

"""Cloud Chain Core test module."""


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
try:
    import ipfsapi
except ModuleNotFoundError:
    os.system("pip install ipfsapi")
    import ipfsapi

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests

# local core library classes and functions are imported via core.main
from core.main import *

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
        #input()
        PRINT_IPFS_DEBUG_INFO(__ipfs_bitswap_stat)
        #input()
        PRINT_IPFS_DEBUG_INFO(__ipfs_swarm_peers)
        #input()
        PRINT_IPFS_DEBUG_INFO(__ipfs_swarm_addrs)







def test_ALL():
    test_IPFS()

if __name__ == "__main__":
    test_ALL()