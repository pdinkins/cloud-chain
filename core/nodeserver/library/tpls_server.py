# NODE $ERVER$Y$TEM ## TPLS SERVER # 
'''
functional implementation of the 'transport layer security sever' or tpls_server

this code works for the most part

when i wrote this only God and I understood it. 
now only God does

TODO : FIX THIS
'''
import logging
import datetime as dt
import logging
import sys
import socketserver
import socket
import os
import inspect

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

class config:
    def __init__(self):
        self.ip = '192.168.1.7'
        self.port = 1423
        self.tw = ['tpls']

node = config()

local_ip = node.ip
n_port = node.port
tw = node.tw
trusted_wallet_hash = node.tw
handshake = []
run = True


def chash_0(input_string):  
    handshake.clear()
    autolog('chash_0: input')
    packet = input_string
    for i in range(0, len(tw)) or packet == tw[i]:
        if packet != tw[i]:
            cs = 'ERROR: CONNECTION UNSUCCESSFUL'
            handshake.clear()
            handshake.append(0)
            autolog(cs)
            autolog(handshake)
            return cs

        elif packet == tw[i]:
            cs = 'CONNECTION SUCCESSFUL'
            handshake.clear()
            handshake.append(1)
            autolog(cs)
            autolog(handshake)
            return cs
        
        else:
            cs = 'ERROR: CONNECTION UNSUCCESSFUL'
            handshake.clear()
            handshake.append(0)
            autolog(cs)
            autolog(handshake)
            return cs

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):
    # incoming user wallet hash, id of user/node
    init_chash_b = conn.recv(MAX_BUFFER_SIZE)
    autolog('client_thread: ')
    # MAX_BUFFER_SIZE is how big the message can be
    siz = sys.getsizeof(init_chash_b)
    if  siz >= MAX_BUFFER_SIZE:
        print("The length of input is probably too long: {}".format(siz))
    autolog('client_thread: ')
    # decode incoming user hash 
    chash_0_r = init_chash_b.decode("utf8")
    autolog(chash_0_r)
    # analyze incoming user hash
    res = chash_0(chash_0_r)
    autolog('chash -> analyer')
    vysl = res.encode("utf8")  # encode the result string
    conn.sendall(vysl)  # send it to client
    # check the handshake status and execute functions based on it
    if handshake[0] == 1:
        # fid tx
        autolog('FID INCOMING')
        data_bytes = conn.recv(MAX_BUFFER_SIZE)
        siz = sys.getsizeof(init_chash_b)
        if  siz >= MAX_BUFFER_SIZE:
            print("The length of input is probably too long: {}".format(siz))
        # decode the FID 
        data = data_bytes.decode('utf-8')
        autolog(data)
        fid_analyze(data)
        # responce after fid execute
        replyb = 'DATA TRANSFER COMPLETE'
        conn.sendall(replyb.encode('utf-8'))
    # close all the connections
    else:
        conn.close()  # close connection
        arnold = 'CONNECTION ' + ip + ':' + port + " TERMINATED"
        autolog(arnold)


def fid_analyze(fid):
    msg = 'FID: ' + str(fid)
    autolog(msg)
    if fid == '0':
        autolog('0_NETWORK_PROTOCOL')
    elif fid == 'ipfs':
        os.system('start ipfs daemon')
    elif fid == '1':
        autolog('1_np')
    else:
        autolog('NO MATHCING FID EXECUTABLES')

def post_fid_anal():
    pass


def start_handshake():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    autolog('SOCKET CREATED')

    try:
        soc.bind((local_ip, n_port))
        autolog('SOCKET BIND COMPLETE')
    except socket.error as msg:
        # TODO: move this import out of the function
        import sys
        print(dt.datetime.now(), 'BIND_FAIL_ERROR: ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    autolog('SOCKET LISTENING')
    
    # for handling task in separate jobs we need threading
    #  TODO: move this import out of the function
    from threading import Thread

    # this will make an infinite loop needed for 
    # not reseting server for every client

    conn, addr = soc.accept()
    ip, port = str(addr[0]), str(addr[1])
    d = 'loop_0 > ACCEPTING CONNECTIONS FROM ' + ip + ':' + port
    autolog(d)
    try:
        Thread(target=client_thread, args=(conn, ip, port)).start()
    except:
        print(dt.datetime.now(), "Terible error!")
        import traceback
        autolog('loop: ERROR')
        traceback.print_exc()
    
    soc.close()
    

def autolog(message):
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.debug("{}\t{}\t{}\t{}".format(
        dt.datetime.now(),
        func.co_filename,
        func.co_name,
        message
    ))


class TPLS_Server:
    '''
    This class will create a socket server with the handshake 
    interface from the tpls_server module. This class replaces the 
    functional implementation of the tpls server. 
    
    '''
    import socket as soc
    from threading import Thread

    def __init__(self, ip, port):
        self.logger = logging.getLogger('Tpls_Server')
        self.logger.debug('__init__')
        self._ip = ip
        self._port = port
        self._socket_tup = (self._ip, self._port)
        self.__trusted_hashes = ['tpls']
        self.open_socket()
        

    # Restful functions #
    def _decode(self, arg):
        self.logger.debug('_decode')
        return arg.decode('utf-8')
    
    def _encode(self, arg):
        self.logger.debug('_encode')
        return arg.encode('utf-8')
    
    def _check_size(self, bytes_object, MAX_BUFFER_SIZE = 4096):
        self.logger.debug('_check_size')
        return sys.getsizeof(bytes_object)


    # Active Functions #
    def open_socket(self):
        self.logger.debug('open_socket')
        # TODO: add security / config loading
        self._socket = self.soc.socket(self.soc.AF_INET, self.soc.SOCK_STREAM)
        self._socket.setsockopt(self.soc.SOL_SOCKET, self.soc.SO_REUSEADDR, 1)
        self._socket.bind(self._socket_tup)
        self.__ip_info = str('Node IP:PORT\t') + str(self._socket_tup)
        self.logger.debug('open_socket._socket.bind')
        self.logger.debug(self.__ip_info)
        self._socket.listen(10)
        self.conn , self.addr = self._socket.accept()
        self._ip_ , self._port_ = str(self.addr[0]), str(self.addr[1])
        self.logger.debug('IP: ' + str(self._ip_) + ' PORT: ' + str(self._port_))
        self.Thread(target=self.client_thread, args=(self.conn, self._ip_, self._port_)).start()
    
    def client_thread(self, conn, ip, port, MAX_BUFFER_SIZE = 4096):
        self.logger.debug('client_thread')
        self.incoming_client_hash = self.conn.recv(MAX_BUFFER_SIZE)
        self.incoming_client_hash_size = self._check_size(self.incoming_client_hash)
        self.client_hash = self._decode(self.incoming_client_hash)
        self.logger.debug(self.client_hash)
        print(self.client_hash)
        self._client_hash_analyzer(self.client_hash)

    def _client_hash_analyzer(self, chash):
        for i in range(0, len(self.__trusted_hashes)) or chash == self.__trusted_hashes[i]:
            if chash != self.__trusted_hashes[i]:
                return "fail"
            elif chash == self.__trusted_hashes[i]:
                # self.__client_hash_pass = 1397             
                # return self.__client_hash_pass
                return "pass"
            else:
                self.logger.debug("self._client_hash_analyze()")
                return False


