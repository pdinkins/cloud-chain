import hashlib
import pynetwork.wallet as wallet 

class Packet:
    def __init__(self):
        self.wallet_hash = wallet.wallet_data[0]
        self.data = self.datagen()
        self.hash = self.__hash__()

    def __hash__(self):
        #return hash(self.data)
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8'))
        return sha.hexdigest()

    def datagen(self):
        self.packet_data = str(input('FID> '))
        return self.packet_data


def wallet_genesis():
    wallet.generate_new_wallet()
    wallet.print_cw()
    wallet.write_wallet()

SETUP_PrintPacket = True

def packet_genesis():
    wallet.parse_wallet()
    p = Packet()
    
    if SETUP_PrintPacket:
        print('wallet hash: ', p.wallet_hash)
        print('wallet data', p.data)
        print('wallet data hash', p.hash)
    
    else:
        print('SETUP_PrintPacket = ', SETUP_PrintPacket)
    
    packet2send = [p.wallet_hash, p.data, p.hash]
    return packet2send
