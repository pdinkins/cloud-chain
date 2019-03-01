# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.branchingblockchain.demo"
__version__ = "0.1.3"

# BBC DEMO
# Demonstrates class logic for the genesis chain model
import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
    self.next_hash = self.hasher()

  def hasher(self):
      sha = hasher.sha256()
      sha.update(str(self.previous_hash).encode('utf-8') +
                 str(self.hash).encode('utf-8'))
      return sha.hexdigest()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index).encode('utf-8') +
               str(self.timestamp).encode('utf-8') +
               str(self.data).encode('utf-8') +
               str(self.previous_hash).encode('utf-8'))
    return sha.hexdigest()


class nBlock:
    def __init__(self, hash):
        self.hash = previous_block.next_hash
        self.previous_hash = previous_block.hash
        self.next_hash = self.nhash()

    def nhash(self):
        sha = hasher.sha256()
        sha.update(str(self.previous_hash).encode('utf-8') +
                 str(self.hash).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
  return Block(0, date.datetime.now(), "Genesis Block", "0")

# Generate all later blocks in the blockchain
def next_block(last_block):
  this_hash = last_block.next_hash
  return nBlock(this_hash)




genesis = create_genesis_block()

blockchain = [genesis]

previous_block = blockchain[0]

num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  
  # final data format for block
  print('prev: {}'.format(block_to_add.previous_hash))
  print("Hash: {}".format(block_to_add.hash))
  print('next: {}\n'.format(block_to_add.next_hash))
