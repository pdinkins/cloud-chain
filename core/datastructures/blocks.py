# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.datastructures.blocks"
__version__ = "0.1.3"

class Genesis_Block:
    import datetime
    import hashlib as hasher

    def __init__(self, data):
        self.index = 0
        self.genesis_data = data
        self.timestamp = self.__timestamp()
        self.current_hash = self.__current_hash()
    
    def __timestamp(self):
        return self.datetime.datetime.now()

    def __current_hash(self):
        sha = self.hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') + 
                   str(self.genesis_data).encode('utf-8'))
        return sha.hexdigest()

class Block:
    import hashlib as hasher
    def __init__(self, previoushash, currenthash):
        self.previous_hash = previoushash
        self.current_hash = currenthash
        self.next_hash = self.next_bhash()
        self.header = self.header

    def next_bhash(self):
        shha = self.hasher.sha256()
        shha.update(str(self.previous_hash).encode('utf-8') +
                    str(self.current_hash).encode('utf-8'))
        return shha.hexdigest()
