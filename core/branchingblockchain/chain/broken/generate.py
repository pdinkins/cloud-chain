##############  BROKEN ##################
# generate
# Functions for generating blocks on the genesis chain
# beware when venturing foward
# you will get a headache
# Use this for logic referance


from blocks import Genesis_Chain, Block
import chain
import writer
import network


# generate the genesis block
def g_g_block():
    genesis_chain_g_block = Genesis_Chain().generate_genesis_block()
    return genesis_chain_g_block

def initailize_new_genesis_chain(ledgername):
    # input ledger name
    # ledgername = input('ledger name: ')
    # create ledger file and ledger object for filename reference
    ledger = writer.NewLedger(ledgername)
    # generate the genesis block
    genesis_block = g_g_block()
    # add genesis block to the block chain list
    chain.blockchain.append(genesis_block)
    # print genesis block info
    print_block(chain.blockchain,0)
    # generate genesis block value list
    gblocklist = [genesis_block.previous_hash,
                    genesis_block.current_hash,
                    genesis_block.next_hash]
    # write genesis block to ledger
    writer.ledger_constructor(ledger.filename, gblocklist)

'''
#TODO: determine if both of these functions are necessary. i think not but science is neeeded
'''

def initailize_genesis_chain(ledgername):
    ###### DANGER THIS FUNCTION WILL CREATE A NEW GENESIS BLOCK ON THE SELECTED LEDGER
    #### USE ONLY FOR FRESH LEDGER OR USE initailize_new_genesis_chain()
    ledger = writer.Ledger(ledgername)  # create ledger object for filename reference
    genesis_block = g_g_block()         # generate the genesis block
    chain.blockchain.append(genesis_block)  # add genesis block to the block chain list
    print_block(chain.blockchain,0)     # print genesis block info
    gblocklist = [genesis_block.previous_hash, genesis_block.current_hash, genesis_block.next_hash]    # generate genesis block value list
    writer.ledger_constructor(ledger.filename, gblocklist)  # write genesis block to ledger


# generating new blocks on the genesis chain
def new_block(ledgerfilename):
    # ledger class instance for file name reference
    ledger = writer.Ledger(ledgerfilename)
    # parse the selected ledger
    writer.ledger_parse(ledger.filename)
    # data gets stored in lists in module chain.py
    l = bc_l()  # blockchain length calc
    l -= 1
    # generate the next block in the chain
    newblock = Block(chain.c_hash[l], chain.n_hash[l])
    chain.blockchain.append(newblock)
    nblocklist = [newblock.previous_hash,
                    newblock.current_hash,
                    newblock.next_hash]
    #TODO: concensus check to eliminate duplicate blocks
    # add new block to the ledger
    writer.ledger_constructor(ledger.filename, nblocklist)


# determines the length of the blockchain
def bc_l():
    length = len(chain.blockchain)
    return length


# print the genesis block data
def print_gblock(gblockname):
    print(gblockname)
    print('previous:{}\ncurrent:{}\nnext:{}\n'.format(gblockname.previous_hash,
                                                        gblockname.hash,
                                                        gblockname.next_hash))

# print any block in the chain
def print_block(blockchainlist, index):
    block = blockchainlist[index]
    print('\n{}\n{}\n{}\n{}'.format(block, block.previous_hash, block.current_hash, block.next_hash))


