# -*- coding: utf-8 -*-

"""core.ipfs.main module."""

# IMPORTS #
# python library imports
import subprocess
import time
import os

# third party package imports
import ipfsapi

class CORE_IPFS:
    def __init__(self):
        self.core = self.__return_core
    
    def __return_core(self):
        self.__core = "CORE_IPFS.core"
        return self.__core

class IPFS_NODE:
    def __init__(self, NodeID, PublicKey, PrivateKey):
        self.NodeId = NodeID
        self.PubKey = PublicKey
        self.PriKey = PrivateKey



def IPFS_API_CONNECTION():
    # this function requires that an ipfs node daemon be running
    # also assumes the api address is set to default
    # return ipfs api connnection via the py-ipfs-api packages
    try: 
        return ipfsapi.connect("127.0.0.1", 5001)
    except ConnectionRefusedError:
        return ipfsapi.connect("127.0.0.1", 5002)

def PRINT_IPFS_DEBUG_INFO(dictobj):
    # create a list of the keys for the given dictionary
    dictkeys = list(dictobj.keys())
    # loop over the dictionary and print the data 
    for i in range(0, len(dictkeys)):
        print(dictkeys[i], ' ', dictobj[dictkeys[i]])

def LAUNCH_SP_IPFS_DAEMON():
    return subprocess.run(["ipfs", "daemon"])

def LAUNCH_IPFS_DAEMON():
    # spawn ipfs daemon instance in another command prompt window
    os.system("start ipfs daemon")


## OUTDATED LEGACY ##
class IPFS_API:
    '''
    ipfsnode = Ipfs_API()
    '''
    def __init__(self):
        self.ipfslist = ['Addresses', 'ID', 'AgentVersion', "ProtocolVersion", "PublicKey" ]
        self.ipfsapi_ip = '127.0.0.1'
        self.ipfsapi_port = 5001
        self.ipfsapi_port2 = 5002
        self.debug = False
        self._api_connection = self.__initialize_ipfsapi_connection()
        self._api_id_info = self.__api_id_info
        self.reader = self._ipfs_reader
        self.writer = self._ipfs_writer
        self.bitswap = self._ipfs_bitswap_stat
        self.ipfs_client = self._ipfs_client

    def __initialize_ipfsapi_connection(self):
        try:
            self.api_connection = ipfsapi.connect(self.ipfsapi_ip, self.ipfsapi_port)
        except ConnectionRefusedError:
            self.api_connection = ipfsapi.connect(self.ipfsapi_ip, self.ipfsapi_port2)
        # api connection instance adopted from the ipfsapi.connect class    
        return self.api_connection
    
    def __api_id_info(self):
        self.apiid = self.api_connection.id()
        self.ipfs_addresses = self.apiid[self.ipfslist[0]]
        if self.debug != False:
            for i in range(1, len(self.ipfslist)):
                print(self.ipfslist[i],'\n' + self.apiid[self.ipfslist[i]] + '\n')
            print(self.ipfslist[0])
            for i in range(0, len(self.ipfs_addresses)):
                print(self.ipfs_addresses[i])

    
    def _ipfs_client(self):
        return self._api_connection

    # used to return file contents from ipfs with given hash value
    def _ipfs_reader(self, _filehash):
        return self._api_connection.cat(_filehash)

    # adds the given file to ipfs using the py-ipfs-api
    def _ipfs_writer(self, _file):
        return self._api_connection.add(_file)

    # grabs the current bitswap_stat dictionary containing list of peers and data usage amounts
    def _ipfs_bitswap_stat(self):
        return self._api_connection.bitswap_stat


__bitswap_stat_dict= [
    'ProvideBufLen', 
    'Wantlist', 
    'Peers', 
    'BlocksReceived', 
    'DataReceived', 
    'BlocksSent', 
    'DataSent', 
    'DupBlksReceived', 
    'DupDataReceived']

def pbs(bssdict):
    for i in range(0, len(bssdict)):
        print(bssdict[__bitswap_stat_dict[i]])