'''
# Network
# contains network related functions
'''
#==============================================================================================#

import logging
import sys
import socketserver

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

class EchoRequestHandler(socketserver.BaseRequestHandler):
    
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        self.logger.debug('setup')
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug('handle')

        # Echo the back to the client
        data = self.request.recv(1024)
        self.logger.debug('recv()->"%s"', data)
        self.request.send(data)
        return

    def finish(self):
        self.logger.debug('finish')
        return socketserver.BaseRequestHandler.finish(self)

class EchoServer(socketserver.TCPServer):
    
    def __init__(self, server_address, handler_class=EchoRequestHandler):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug('__init__')
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        self.logger.debug('server_activate')
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self):
        self.logger.debug('waiting for request')
        self.logger.info('Handling requests, press <Ctrl-C> to quit')
        while True:
            self.handle_request()
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug('verify_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        self.logger.debug('process_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.process_request(self, request, client_address)

    def server_close(self):
        self.logger.debug('server_close')
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        self.logger.debug('finish_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.finish_request(self, request, client_address)

    def close_request(self, request_address):
        self.logger.debug('close_request(%s)', request_address)
        return socketserver.TCPServer.close_request(self, request_address)


class tpls_server:
    '''
    This class will create a socket server with the handshake 
    interface from the tpls_server module. This class replaces the 
    functional implementation of the tpls server. 
    
    '''
    import sys
    import socket as soc
    from threading import Thread

    def __init__(self, ip, port):
        self.logger = logging.getLogger('Tpls_Server')
        self._ip = ip
        self._port = port
        self._socket_tup = (self._ip, self._port)
        self.__trusted_hashes = ['tpls']
        self.chash = self.open_socket()

    def _decode(self, arg):
        return arg.decode('utf-8')
    
    def _encode(self, arg):
        return arg.encode('utf-8')
    
    def _check_size(self, bytes_object, MAX_BUFFER_SIZE = 4096):
        return self.sys.getsizeof(bytes_object)

    def open_socket(self):
        self._socket = self.soc.socket(self.soc.AF_INET, self.soc.SOCK_STREAM)
        self._socket.setsockopt(self.soc.SOL_SOCKET, self.soc.SO_REUSEADDR, 1)
        self._socket.bind(self._socket_tup)
        self._socket.listen(10)
        self.conn , self.addr = self._socket.accept()
        self.__ip , self.__port = str(self.addr[0]), str(self.addr[1])
        self.Thread(target=self.client_thread, args=(self.conn, self.__ip, self.__port)).start()
        
    def client_thread(self, conn, ip, port, MAX_BUFFER_SIZE = 4096):
        self.incoming_client_hash = self.conn.recv(MAX_BUFFER_SIZE)
        self.incoming_client_hash_size = self._check_size(self.incoming_client_hash)
        self.client_hash = self._decode(self.incoming_client_hash)
        return self.client_hash

    def _client_hash_analyzer(self):
        for i in range(0, len(self.__trusted_hashes)) or self.chash == self.__trusted_hashes[i]:
            if self.chash != self.__trusted_hashes[i]:
                return False
            elif self.chash == self.__trusted_hashes[i]:
                return True
            else:
                return False

        

'''
## implementation of the echo server classes

if __name__ == '__main__':
    import socket
    import threading

    address = ("192.168.1.5", 0) # let the kernel give us a port
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address # find out what port we were given

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # don't hang on exit
    t.start()

    logger = logging.getLogger('client')
    logger.info('Server on %s:%s', ip, port)

    # Connect to the server
    logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connecting to server')
    s.connect((ip, port))

    # Send the data
    message = 'Hello, world'
    logger.debug('sending data: "%s"', message)
    len_sent = s.send(message.encode('utf8'))

    # Receive a response
    logger.debug('waiting for response')
    response = s.recv(len_sent)
    logger.debug('response from server: "%s"', response)

    # Clean up
    logger.debug('closing socket')
    s.close()
    logger.debug('done')
    server.socket.close()

'''

