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
import ipfsapi
import requests

# local module imports

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




        

