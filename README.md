# cloud-chain
Main Repository for the Cloud Chain Platform

##  MUST INSTALL ALL OF THE FOLLOWING MODULES ##
    # pdinkins/node-server 
    # pdinkins/terminal-client
    # pdinkins/pythos
    # pdinkins/branching-blockchain

    # go-lang
    # go-ipfs

    # ipfsapi
    # requests


# core 
## Pythos
### Python developmental environment 
Pythos is a platform for creating developmental environments. Pythos is built on top of the branching-blockchain and IPFS. Pythos is still very much in development and needs work. Im working on getting all of the legacy code from the branching-blockchain module refactored, streamlined, and merged into the modules. 

### Modules
*/modules:*   
- /menu
- /ipfs
- /db
- /ntwrk
- /web

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