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


class IPv4_header:
    @staticmethod
    def decipher(data):
        storeobj = unpack("!BBHHHBBH4s4s", data)
        _version = storeobj[0] 
        _tos = storeobj[1]
        _total_length = storeobj[2]
        _identification = storeobj[3]
        _fragment_Offset = storeobj[4]
        _ttl = storeobj[5]
        _protocol = storeobj[6]
        _header_checksum = storeobj[7]
        _source_address = inet_ntoa(storeobj[8])
        _destination_address = inet_ntoa(storeobj[9])
        _data={
            "Version": _version,
            "Tos": _tos,
            "Total Length": _total_length,
            "Identification": _identification,
            "Fragment": _fragment_Offset,
            "TTL": _ttl,
            "Protocol": _protocol,
            "Header CheckSum": _header_checksum,
            "Source Address": _source_address,
            "Destination Address":_destination_address
        }
        return _data


class ETH_header:
    @staticmethod
    def decipher(data):
        storeobj = data
        storeobj = unpack("!6s6sH",storeobj)
        destination_mac = hexlify(storeobj[0])
        source_mac = hexlify(storeobj[1])
        eth_protocol = storeobj[2]
        _data = {
            "Destination Mac":destination_mac,
            "Source Mac":source_mac,
            "Protocol":eth_protocol
        }
        return _data


class ICMP_header:
    @staticmethod
    def decipher(data):
        icmph = unpack('!BBH', data)
        icmp_type = icmph[0]
        code = icmph[1]
        checksum = icmph[2]
        _data = {
            'ICMP Type':icmp_type,
            "Code":code,
            "CheckSum":checksum
        }
        return _data


class TCP_header:
    @staticmethod
    def decipher(self):
        storeobj = unpack('!HHLLBBHHH',data)
        _source_port = storeobj[0] 
        _destination_port = storeobj[1]
        _sequence_number = storeobj[2]
        _acknowledge_number = storeobj[3]
        _offset_reserved = storeobj[4]
        _tcp_flag = storeobj[5]
        _window = storeobj[6]
        _checksum = storeobj[7]
        _urgent_pointer = storeobj[8]
        _data = {
            "Source Port":_source_port,
            "Destination Port":_destination_port,
            "Sequence Number":_sequence_number,
            "Acknowledge Number":_acknowledge_number,
            "Offset & Reserved":_offset_reserved,
            "Tcp Flag":_tcp_flag,
            "Window":_window,
            "CheckSum":_checksum,
            "Urgent Pointer":_urgent_pointer
        }
        return _data

class MAC_ADDRSS:
    @staticmethod
    def mac_formater(a):
        raw_mac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
        return raw_mac