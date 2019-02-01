# NODE $ERVER$Y$TEM ## NODE #
# -------- IMPORTS --------- # 
# Local imports
from library import tpls_server
from library import ipfs

# python builtin imports
import os
import time

# third party package imports
#import ipfsapi
# -------------------------- # 


_node_help =     """
    The node server adopts from multiple different classes.
    Gate keeper for private networks. Facilitates custom user functions. 

    IPFS Daemon must be running 
    IPFSAPI_IP: 127.0.0.1:5001/5002

    > Node
        > client interface
            - user input
        > httpserver
            - filehosting
            - filestorage
        > ipfs node(daemon)
            - read
            - write
        > tpls_server
            - network communications
    
    > Post config file creation 
        > network config
        > ipfs id
        > node wallet
            > trusted peers
            > data store hashes

    """

def nodehelp():
    print(_node_help)

class NodeServer:
    '''
    NodeServer
    '''
    def __init__(self):
        self._http_server = self.__http_server
        self.__ipfs_node()
        self._ipfs_client_interface = self.__client_interface
        self._tpls_server = self.__tpls_server
        self._cli_dir = self.__client_interface_dir
        # TODO: get rid of these or figure out a better use
        # local bool variable to control what the node server launches on start up
        #_b_http = True
        #_b_ipfs = True
        #_b_cli = True
        #_b_tpls = True

        # TODO: generate these variables from the config file
        # node networking variables
        self._0_node_ip = "192.168.1.x"
        self._0_node_port = 11111

    

    # Launch HTTP server
    def __http_server(self):
        # TODO: add multiplatform support, aswell as security options
        os.system("start py -m http.server --bind 127.0.0.1")
        
    # Launch IPFS Daemon
    def __ipfs_node(self):
        # Determines whether or not debug shell is displayed on launch of ipfs daemon instance
        __debug = False 
        # TODO: add multiplatform functionalality to this asap
        if __debug:
            os.system("start ipfs daemon --debug")
        else:
            os.system("start ipfs daemon")
        # 3 second delay to allow the daemon to start up
        time.sleep(3)
        # test ipfs api connection; displays some debug info
        #self.__ipfsnode = ipfs.IPFS_API()

    # Instantiates an PY-IPFS-API client object
    def __client_interface(self):
        # elevates ipfsapi.client.Client() namespace for use locally within this module
        self.__ipfs_client = ipfs.IPFS_API()._ipfs_client() 
        return self.__ipfs_client
    
    # Create different types of TPLS Server instances
    def __tpls_server(self, _type):
        # functional transport layer security server
        # begin one time functional tpls instance
        if _type == 0:
            return tpls_server.start_handshake()
        # begin an infinite loop of functional tpls instances
        elif _type == 1:
            while True:
                tpls_server.start_handshake() 
        # tpls class instance; not as developed as the functional 
        elif _type == 2:
            # OOP implementation of the TPLS Server
            tpls_server.TPLS_Server(self._0_node_ip, self._0_node_port)
        # end all catch all; reduces errors
        else:
            # TODO: add further error handling, and tplss options
            return 0
    

    def __client_interface_dir(self):
        # returns list of all the IPFSAPI class methods
        return dir(self.__client_interface())
