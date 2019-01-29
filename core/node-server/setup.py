# NODE $ERVER$Y$TEM ## SETUP #
'''
# SETUP
#
# sniffs current build and generates current config file
# configures and installs ipfs
#
# import setup
# 
# user = setup.UserBuild()
'''
# ------ IMPORTS ------ #
# python module imports
import platform
import os

# local lib imports
from library._log import log
from library.writer import FileObject, Write2file
from library.classes import Location

# third party package imports
from requests import get


# USER BUILD 
class UserBuild:
    '''
        # sniff current cpu system configuration 
        # establish configuration information
        1. ip address
        2. operating system
        3. cpu information
        4. python config 
        5. ipfs config
        6. requirements config
        # TODO: check for corrupted or out of date software
    '''
    def __init__(self):
        self.opsys = platform.system()
        self.__location = Location()
        self.ip = self.__location.ip
        self.pyver = platform.python_version

def setup_ipfs():
    # requires installed package managers
    # windows install (choco)
    if Node.opsys == 'Windows':
        os.system("choco install go")
        os.system("choco install ipfs")

    # mac install (home brew)
    elif Node.opsys == "Darwin":
        os.system("brew install go")
        os.system("brew install ipfs")


if __name__ == "__main__":
    Node = UserBuild()

