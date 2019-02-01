import socket
import sys

def socket_create():
    try:
        global host
        global port 
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(msg)

def socket_bind():
    try:
        global host
        global port 
        global s
        host = ''
        port = 9999
    
    except socket.error as msg:
        print(msg)

