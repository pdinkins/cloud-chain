# -*- coding: utf-8 -*-

"""core module."""

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
from core.ipfs.main import IPFS_API, IPFS_API_CONNECTION, pbs
from core.terminalclient.main import Interface


# Github Repositories 
gitrepo_go_ipfs = "https://github.com/ipfs/go-ipfs.git"
gitrepo_ripple = "https://github.com/ripple/rippled.git"
gitrepo_ripple_net_crawler = "https://github.com/ripple/rippled-network-crawler.git"

# config data
__config = {
        "user":[],
        "ipfshash":[],
        "ip":[],
        "google":[],
        "facebook":[],
        "twitter":[],
        "instagram":[],
        "discord":[],
        "github":[],
        "gitlab":[],
        "pinterest":[],
        "skype":[]}


def __write_config_file():
    with open("cfg.cfg", 'w') as cfgfile:
        cfgfile.write(str(__config))


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