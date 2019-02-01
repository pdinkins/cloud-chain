"""
Client 

Top layer CLI for the branching-blockchain platform.

Read through the modules in this library for more in depth 
documentation. Python is meant to be a readable language and this project aims
to keep that standard. By that regard, documentation for this project will 
be offered exclusively in the source. 
"""

from chain import _client
from os import system

def clone_repo():
    # This module only acts as a repo updater. Checking for new source
    # and updating automatically.Acts as a light consensus module for 
    # source control functions executed directly by the network. 

    system('git clone https://github.com/pdinkins/branching-blockchain.git')

def demo():
    system('py demo.py')


def _menu_init():
    _client.mm()
