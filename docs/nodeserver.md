## Node-Server
The node server adopts from multiple different classes. Gate keeper for private networks. Facilitates custom user functions. 

    command : description 
    0: logout
    1: main menu
    2: networking menu 
    3: python shell
    tpls: transport level security server
    help: help menu (you are here)

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

v0.0.49