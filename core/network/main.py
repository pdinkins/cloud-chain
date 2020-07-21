# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.main"
__version__ = "0.1.3"

from core.network.server.main import SERVER
from core.network.client.main import CLIENT
from core.network.config.main import *
from core.network.utils import ingest

class CORE_NETWORK:
    def __init__(self):
        self.ip = HOST._get_host_ip()


class network:
    """
    Networks consist of a collection of nodes. Each node has a list of peers that
    it communicates with. 

    """
    def __init__(self):
        self.load_nodes()
    
    def load_nodes(self):
        pass


class node:
    '''
    A node is a single entity within the network. A node can be a single computer 
    or multiple within the same LAN.

    ip: must be an ip object
    peers: list of ip's

    '''
    def __init__(self, ip, peers):
        self.ip = str(ip) 
        self.peers = list(peers)

class peer:
    '''
    A peer is a node that is trusted by another node in the network. Data is transmitted directly
    to peers from node through sockets. 

    ip: must be an ip object
    '''
    def __init__(self, ip):
        self.ip = ip
        if self.ip.object:
            print("object test pass")
        else: 
            print("object test fail. you must use an ip object")

class ip:
    '''
    This class is used to create a single data structure to use when working with ip addresses.

    The octect are passed when the class is created and then the .address attribute allows for 
    easy use of the ip object for others functions.
    '''
    def __init__(self, octet1, octet2, octet3, octet4):
        self.octet1 = str(octet1)
        self.octet2 = str(octet2)
        self.octet3 = str(octet3)
        self.octet4 = str(octet4)
        self.ipaddress = self.__ipaddress()
        self.object = True

    def __ipaddress(self):
        self.__ip = str(
            self.octet1 + '.' +
            self.octet2 + '.' +
            self.octet3 + '.' +
            self.octet4)
        return self.__ip

def test_network():
    c = CORE_NETWORK()
    while True:
        pcks = ingest.INGEST(c.ip)._return_raw_packets()
        print(pcks)

if __name__ == "__main__":
    c = CORE_NETWORK()
    while True:
        pcks = ingest.INGEST(c.ip)._return_raw_packets()
        print(pcks)
