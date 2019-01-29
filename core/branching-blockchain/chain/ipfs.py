'''
# IPFS
# interact with the ipfs network 
# 
# This module makes use of the py-ipfs-api to interact with
# an ipfs node. 
 
'''

import ipfsapi
import requests


class Ipfs_API:
    '''
    USE:
        # first initialize the connection
        ipfsnode = Ipfs_API()

    '''
    def __init__(self):
        # initial variables
        self.ipfslist = ['Addresses', 'ID', 'AgentVersion', "ProtocolVersion", "PublicKey" ]
        self.ipfsapi_ip = '127.0.0.1'
        self.ipfsapi_port = 5002

        # sub level variables
        self._api_connection = self.initialize_ipfsapi_connection()

    def initialize_ipfsapi_connection(self):
        # establish 
        self.api = ipfsapi.connect(self.ipfsapi_ip, self.ipfsapi_port)
        self.apiid = self.api.id()
        self.ipfs_addresses = self.apiid[self.ipfslist[0]]
        for i in range(1, len(self.ipfslist)):
            print(self.ipfslist[i],'\n' + self.apiid[self.ipfslist[i]] + '\n')
        print(self.ipfslist[0])
        for i in range(0, len(self.ipfs_addresses)):
            print(self.ipfs_addresses[i])
        
        # return the api connection instance 
        # adopted from the ipfsapi.connect class    
        return self.api

class IPFS_add_file:
    '''
    # add the file to the ipfs network
    '''
    def __init__(self, _file):
        self.ipfsapi_init = Ipfs_API()
        self.api_connection = self.ipfsapi_init._api_connection
        self._file = _file
        self._file_hash = self.add_file()

    def add_file(self):
        self.file2add = self.api_connection.add(self._file)
        self.__filehash = self.file2add["Hash"]
        # ensure the transfer went through by printing the filehash and file contents
        print(self.__filehash)
        print(self.api_connection.cat(self.__filehash))
        return 





'''
TODO: Fix all of these functions lol 


def add_file(filename):
    api = ipfsapi.connect(ipfsapi_ip, ipfsapi_port)
    file2add = api.add(filename)
    filehash = file2add["Hash"]
    print(filehash)
    #print(api.cat(file2add['Hash']))
    req = requests.get('https://gateway.ipfs.io/ipfs/' + filehash)
    print(req.text)
    return filehash


def upload_g_chain():
    name = input('ledger>\t')
    ledger = writer.Ledger(name)
    add_file(ledger.filename)


def ipfs_ledger_deconstruct():
    data, nhash = ipfs_ledger_getter()
    #generate.initailize_new_genesis_chain(nhash)
    ledger = writer.Ledger(nhash)
    with open(ledger.filename, 'wb') as file:
        file.write(data)
    writer.ledger_parse(ledger.filename)
    print(chain.c_hash)


def ipfs_daemon_init():
    # opens new terminal shell and initailizes the IPFS daemon
    subprocess.Popen([sys.executable, 'ipfsdaemon.py'], shell=True)
    # pause to allow ipfs daemon to begin 
    time.sleep(3)
    # print ipfs data and daemon init confirmation
    initialize_ipfsapi()

def ipfs_ledger_getter():
    network_hash = input('Network hash>\t')
    ipfs_daemon_init()
    api = ipfsapi.connect(ipfsapi_ip, ipfsapi_port)
    req = requests.get('https://gateway.ipfs.io/ipfs/' + network_hash)
    network_ledger_data = req.text
    print(network_ledger_data)
    rawdata = api.cat(network_hash)
    return rawdata, network_hash

'''
