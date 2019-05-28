# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.utils.main"
__version__ = "0.1.3"

from socket import inet_ntoa
from struct import unpack
from binascii import hexlify

class PACKET_HEADERS:
    def __init__(self):
        self.IPv4 = self._IPv4()
        self.ETH = self._ETH()
        self.ICMP = self._ICMP()
        self.TCP = self._TCP()
        self.UDP = self._UDP()

    def _IPv4(self):
        self.__header = IPv4_header()

    def _ETH(self):
        self.__header = ETH_header()

    def _ICMP(self):
        self.__header = ICMP_header()

    def _TCP(self):
        self.__header = TCP_header()

    def _UDP(self):
        self.__header = UDP_header()

