# NODE #
# $ERVER$Y$TEM #
# PYSCANNER_3 # 

# -------- IMPORTS --------- # 
import socket

# sets the range of the final digit in the ip address
# assumes the begining of the ip is '192.168.1.' 
__lowIP = 1
__highIP = 200 

# sets the range for the number of ports to scan
# run the script a few times and fine tune the range for better results
__lowPort = 1
__highPort = 5000

# socket timeout in (s)
# decreasing the time may decrease execution time but 
# will sacrifice accuracy when scanning targets. 
# some ips and ports may not respond as fast as others 
__timeout = 0.0000001


def scan_host_ip(host):
    # main function that scans the network for open ports
    print('  [*]scan_host_ip: ', host, end='\r')
    # set the port scan range 
    ports = range(__lowPort, __highPort)
    for port in ports:
        try:
            print("  [+] Connecting to " + host + ":" + str(port), end='\r')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(__timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                print("  [*]OPEN___________" + host + ':' + str(port))
            s.close()
        except KeyboardInterrupt:
            quit()

def main():
    base_host_ip = "192.168.1."
    base_host_ip_fd = range(__lowIP, __highIP)
    _hosts = []

    for i in base_host_ip_fd:
        __host = str(base_host_ip) + str(i)
        # print("preparing the IP's", __host)
        _hosts.append(__host)

    for j in range(0, len(_hosts)):
        scan_host_ip(_hosts[j])

if __name__ == "__main__":
    main()
