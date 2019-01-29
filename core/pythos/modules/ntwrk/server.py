# server.py
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s', )
import datetime as dt
import logging
import sys
import socketserver

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )


local_ip = "127.0.0.1"
n_port = 1234
tw = ['22670bf1b10545e46f7d797c8e4bd7a77af1bb667f7e864aaca07fad65439f84','951c49bc88ce9a2cc31d4470423590a7c0bedbef953a06a72e6b5d4f74731ed6', '56b8ba882b6aeeb7fa43f9125d8d2909b8a734f82b46b67b3809105a28cfb05d']
trusted_wallet_hash = tw
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
    import sys
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
       
    else:
        conn.close()  # close connection

    arnold = 'CONNECTION ' + ip + ':' + port + " TERMINATED"
    autolog(arnold)
    start_handshake()


def fid_analyze(fid):
    autolog(type(fid))
    if fid == '99':
        autolog(fid)
        run = False
    elif fid == '0':
        # pipe to execute function
        autolog('0_NETWORK_PROTOCOL')

    elif fid == '1':
        autolog('1_np')
    elif fid == 'msg':
        incoming_msg(fid)
    else:
        autolog('NO MATHCING FID EXECUTABLES')

def post_fid_anal():
    pass
    


def incoming_msg(msg):
    autolog(msg)


def start_handshake():
    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    autolog('SOCKET CREATED')

    try:
        soc.bind((local_ip, n_port))
        autolog('SOCKET BIND COMPLETE')
    except socket.error as msg:
        import sys
        print(dt.datetime.now(), 'BIND_FAIL_ERROR: ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    autolog('SOCKET LISTENING')
    # for handling task in separate jobs we need threading
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
    import inspect, logging
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
