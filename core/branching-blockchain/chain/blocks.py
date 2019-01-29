'''
# BLOCKS
# block creation related functions

USE:
    1. import blocks
    2.
'''


class Genesis_Block:
    '''
    In the begining there was light.
    The genesis block is the begining of any data flow through the branching-blockchain system.
    This block is the begining and contains the anchor hash for the proceding block.
    Every chain begins with a Genesis_block object. 
    '''
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
    '''
    Block is the very highest abstraction in the branching blockchain model.
    The previous and current hash are required args to instantiate a Block object.
    A block object references the next hash in the sequence.
    '''
    import hashlib as hasher
    def __init__(self, previoushash, currenthash):
        self.previous_hash = previoushash
        self.current_hash = currenthash
        self.next_hash = self.next_bhash()

    def next_bhash(self):
        shha = self.hasher.sha256()
        shha.update(str(self.previous_hash).encode('utf-8') +
                    str(self.current_hash).encode('utf-8'))
        return shha.hexdigest()

