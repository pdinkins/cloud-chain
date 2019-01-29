import sys
from socket import socket, AF_INET, SOCK_STREAM

SERVER_IP   = '192.168.1.7'
PORT_NUMBER = 1423
SIZE = 4096
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

dataa = input('data to send> ')

def soc():
        mySocket = socket( AF_INET, SOCK_STREAM )
        mySocket.connect((SERVER_IP, PORT_NUMBER))
        return mySocket

while True:
        mySocket = soc()
        mySocket.send(dataa.encode('utf-8'))
        d = mySocket.recv(SIZE)
        dd = d.decode('utf-8')
        print(dd)
        mySocket.close()
 

sys.exit()