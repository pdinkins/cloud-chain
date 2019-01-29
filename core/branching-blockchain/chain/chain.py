'''
# CHAIN
# Stores current blockchain information and chain functions
# All storage is dynamic and is determined by the users actions


'''
from logger import log
from blocks import Genesis_Block

class Blockchain:
    '''
    # contains block objects
    '''
    def __init__(self):
        # dynamic list
        self.chain = []
        self.current_transactions = 0
        self.genesis_block = self.generate_genesis_block()


    def start_chain(self):
        self.chain.append(self.genesis_block)
        self.check = self.current_transactions + self.genesis_block.index
        if self.check == 0:
            self.new_block()

    def generate_genesis_block(self):
        self.gb = Genesis_Block('genesis')
        return self.gb

    def new_block(self):
        # pipe in the next nodes block data
        self.__block = self.__pipe_4_block()
        
        return self.__block
    
    def __pipe_4_block(self):
        return True

    @property
    def current_block(self):
        return True

    @property
    def last_block(self):
        return True
        

