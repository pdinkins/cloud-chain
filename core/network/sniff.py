import socket 

__debug = True

def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        if __debug:
            print(host_name, host_ip)
        return host_ip
    except:
        print("fail haha fuk u")

hostip = get_host_ip()
soc2sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
soc2sniff.bind((hostip, 0))
soc2sniff.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
soc2sniff.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while True:
    print(soc2sniff.recvfrom(65565))