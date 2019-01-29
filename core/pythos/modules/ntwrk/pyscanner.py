# pyscanner
from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 5000
min_port = 1

def scan_host(host, port, r_code = 1):
	try:
		soc = socket(AF_INET, SOCK_STREAM)
		soc.settimeout(0.5)
		code = soc.connect_ex((host, port))

		if code == 0:
			r_code = code
		soc.close()

	except Exception as e:
		print(e)
		pass

	return r_code

try:
	host = input('[*] Enter target host address: ')
except KeyboardInterrupt:
	print('KeyboardInterrupt')
	sys.exit(1)

hostip = gethostbyname(host)
print('\n[*] Host: %s IP: %s' % (host, hostip))
print('[*] Scanning started at %s...\n' % (time.strftime('%H:%M:%S')))
start_time = datetime.now()

for port in range(min_port, max_port):
	try:
		response = scan_host(hostip, port)
		if response == 0:
			print('[*] Port: %d: Open' % (port))
	except Exception as e:
		print(e)
		pass

stop_time = datetime.now()
total_time = stop_time - start_time
print('\n[*] Scan finished at %s' % (time.strftime('%H:%M:%S')))
print('[*] Scan duration: %s' % (total_time))
print('[*] PyScanner')




