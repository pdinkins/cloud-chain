# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.config.main"
__version__ = "0.1.3"

# IMPORTS 
# python library imports 
import os
import sys
import platform

# core config data class
class CORE_CONFIG:
    def __init__(self):
        self.os = self.__return_os()
    
    def __return_os(self):
        # return the operationg system with the platform library
        self.__os = platform.platform()
        return self.__os


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
