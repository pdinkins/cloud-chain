# -*- coding: utf-8 -*-

"""Setup main module."""

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

# get the computers ip address
def getip():
    requests.get()