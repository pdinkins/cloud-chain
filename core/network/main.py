# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.main"
__version__ = "0.1.3"

import socket

class CORE_NETWORK:
    def __init__(self):
        self.network = self.__returnnetwork
        self.soc = self.__gen_socket()

    def __returnnetwork(self):
        self.__network = "CORE_NETWORK.network"
        return self.__network

    def __gen_socket(self):
        self.__soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self.__soc
    
    def __con_socket(self, ip, port):
        try:
            if type(ip) == str:
                if type(port) == int:
                    self.__soc_tup = (ip, port)
                    self.soc.connect(self.__soc_tup)
        except TypeError:
            print("ip/port type error")
    
    def __send_socket(self, data):
        try:
            if type(data) == str:
                self.__encoded_data = data.encode("utf-8")
                self.soc.send(self.__encoded_data)
        except TypeError:
            print("data type error, required a string")
