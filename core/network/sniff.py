import socket 

def get_host_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print(host_name, host_ip)
    except:
        print("fail haha fuk u")

get_host_ip()