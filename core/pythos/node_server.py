


class NodeServer:
    """
    ###### 0_NODE_SERVER ######

    The node server adopts from multiple different classes.
    Gate keeper for private networks. Facilitates custom user functions. 

    IPFS Daemon must be running 
    IPFSAPI_IP: 127.0.0.1:5001/5002

    Config file is required
        > network config
        > ipfs id
        > node wallet
            > trusted peers
            > data store hashes

    > Node
        -client interface
            -user input

        -httpserver
            -filehosting
            -filestorage

        -ipfs node(daemon)
            -read
            -write

        -tpls_server
            -config security settings

    """

    def __init__(self, config_file):
        self._configFile = config_file
        self._httpServer = self.__http_server()
        self._ipfsNode = self.__ipfs_node()
        self._clientInterface = self.__client_interface()
        self._tplsServer = self.__tpls_server()

    def __http_server(self):
        # host files bound to tcp port
        # python3 -m http.server --bind 192.168.1.2
        return 0

    def __ipfs_node(self):
        # ipfs node connection through py-ipfs-api
        #
        return 0

    def __client_interface(self):
        # cli or menu based backend interface
        #
        return 0

    def __tpls_server(self):
        # transport layer security server
        # 
        return 0