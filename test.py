# -*- coding: utf-8 -*-

"""test module."""


# DEBUG OPTION
_debug = True

# IMPORTS #
# python library imports 
import os
import sys
import platform
import datetime
import shutil

# third party package imports
import ipfsapi
import requests

# local core library classes and functions are imported via core.main
from core.main import *

if __name__ == "__main__":
    # IPFS API CONNECTION !!! ipfs daemon must be running
    ipfsnode = IPFS_API_CONNECTION()
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