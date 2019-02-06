# -*- coding: utf-8 -*-

"""Cloud Chain Core main module."""

# DEBUG OPTIOM
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
    # Setup Sequence

    # IPFS API CONNECTION 
    ipfsnode = IPFS_API_CONNECTION()

    # IPFS Debug variables from ipfsapi
    __ipfs_bitswap_stat = ipfsnode.bitswap_stat()
    __ipfs_swarm_peers = ipfsnode.swarm_peers()
    __ipfs_swarm_addrs = ipfsnode.swarm_addrs()
    
    # Convert debug variables into python objects for 
    if _debug:
        pbs(__ipfs_bitswap_stat)
    





    # User login sequence 



    # display the main menu
    #mainmenu.display()
    
