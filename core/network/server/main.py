# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.server.main"
__version__ = "0.1.3"

import socket

class SERVER:
    def __init__(self):
        self._ip = self.__host_ip()
        self._port = 1234
        self.__ip_t_c = None
        self.__port_t_c = None
        self.__type_check()
        self._tup = self.__tup_gen()
        self._socket = self.__create_socket()

    def __host_ip(self):
        # TODO: move to network.config
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        return self.host_ip
    
    def __type_check(self):
        try:
            if type(self._ip) == str:
                self.__ip_t_c = True
        except TypeError:
            self.__ip_t_c = False
        
        try:
            if type(self._port) == int:
                self.__port_t_c = True
        except TypeError:
            self.__port_t_c = False
    
    def __tup_gen(self):
        if self.__ip_t_c:
            if self.__port_t_c:
                self.__tup = (self._ip, self._port)
                return self.__tup

    def __create_socket(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self.__socket
    
    def __connect_socket(self):
        try:
            self._socket.connect(self._tup)
        except ConnectionError as error:
            print(error)
    
    def __encode_data(self, data):
        self.__encoded_data = data.encode("utf8")
        return self.__encoded_data
    
    def __send_data(self, data):
        self.__data = self.__encode_data(data)
        self._socket.send(self.__data)