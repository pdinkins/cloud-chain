# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.client.main"
__version__ = "0.1.3"

import socket

testips = ["192.168.0.9"]
SERVER_IP = testips[0]
SERVER_PORT = 3145

class CLIENT:
        def __init__(self):
                raise NotImplementedError


def connect_to_node():
    # establish socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    # connect to open socket server
    soc.connect((SERVER_IP, SERVER_PORT))
    # import packet module
    import pynetwork.packet as packet
    # raw data to send
    p2s = packet.packet_genesis()
    # send encoded c_hash to server node
    soc.send(p2s[0].encode("utf8"))
    # received data
    hs_bytes = soc.recv(4096) # the number means how the response can be in bytes  
    # decoded data
    hs_string = hs_bytes.decode("utf8")  
    if hs_string == 'CONNECTION SUCCESSFUL':
        # send FID 
        soc.send(p2s[1].encode('utf-8'))
        # Rx 
        reply = soc.recv(4096)
        # print rx 
        print(reply.decode('utf-8'))

def open_socket(ip, port):
    newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return newsocket

def connect_socket(soc, ip, port):
    newsocket.connect((ip, port))

