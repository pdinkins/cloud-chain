# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.utils.ingest"
__version__ = "0.1.3"

from core.network.config.main import *
from socket import socket
from socket import AF_INET, SOCK_RAW, IPPROTO_IP, IP_HDRINCL
from socket import SIO_RCVALL, RCVALL_ON

class INGEST:
    def __init__(self, host_ip):
        self.ip = host_ip
        self.ingestion = self._ingestion()
        self._socket_established = False
    
    def _ingestion(self):
        try:
            soc2sniff = socket(AF_INET, SOCK_RAW, IPPROTO_IP)
            soc2sniff.bind((self.ip, 0))
            soc2sniff.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
            soc2sniff.ioctl(SIO_RCVALL, RCVALL_ON)
            self._socket_established = True
            return soc2sniff
        except OSError:
            print("Must use admin shell")
    
    def _return_raw_packets(self):
        while self._socket_established:
            return self.ingestion.recvfrom(65565)