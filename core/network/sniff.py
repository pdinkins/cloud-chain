import socket 
import threading
import pye
import struct
import binascii
import os

__debug = False

def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        if __debug:
            print(host_name, host_ip)
        return host_ip
    except:
        print("FAIL haha fuk u")

def sniff_dat_fukn_shit():
    hostip = get_host_ip()
    soc2sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    soc2sniff.bind((hostip, 0))
    soc2sniff.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    soc2sniff.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    return soc2sniff

def test_dat_shit():
    while True:
        soc = sniff_dat_fukn_shit()
        packet = soc.recvfrom(65565)
        return packet

s = sniff_dat_fukn_shit()
while True:

    # Capture packets from network
    pkt=s.recvfrom(65565)

    # extract packets with the help of pye.unpack class 
    unpack=pye.unpack()

    print("\n\n===&gt;&gt; [+] ------------ Ethernet Header----- [+]")

    # print data on terminal
    for i in unpack.eth_header(pkt[0][0:14]).items():
        a,b=i
        print("{} : {} | ".format(a,b))
    print("\n===&gt;&gt; [+] ------------ IP Header ------------[+]")
    for i in unpack.ip_header(pkt[0][14:34]).items():
        a,b=i
        print("{} : {} | ".format(a,b))
    print("\n===&gt;&gt; [+] ------------ Tcp Header ----------- [+]")
    for  i in unpack.tcp_header(pkt[0][34:54]).items():
        a,b=i
        print("{} : {} | ".format(a,b))

#if __name__ == "__main__":
#    pc = test_dat_shit()
#    print(pc)
    
