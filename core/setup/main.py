# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.setup.main"
__version__ = "0.1.3"

# IMPORTS #
# python library imports
import os 
import sys
import platform
import datetime

# third party package imports
import requests



# setup process
def SETUP():
    env = os.environ()
    cwd = os.getcwd()
    login = os.getlogin()
    return [env, cwd, login]

def DIRPATH():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

def CANPATH(path):
    can_path = os.path.realpath(path)
    return can_path

def DIRNAME():
    dir_name = os.path.dirname(path)
    return dir_name

def GETCWD():
    cwd = os.getcwd()
    return cwd

def CHGDIR(path):
    return os.chdir(path)

def GETCWDFNAME():
    _cwd = GETCWD()
    data = _cwd.split('\\')
    _n = len(data)
    print(data[_n-1])

# get the computers ip address
def getip():
    requests.get()