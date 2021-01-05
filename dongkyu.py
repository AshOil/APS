import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, prev, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev = prev
        self.nonce = nonce
        self.hash = self.generate_hash()

    def generate_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) +
                   str(self.data) + str(self.prev) + str(self.nonce)).encode())
        return sha.hexdigest()

def proof_of_work(block, difficulty=5):
    proof = block.generate_hash()

    while proof[:5] != '0' * difficulty:
        block.nonce += 1
        proof = block.generate_hash()
    return proof, block.nonce

def create_genesis_block():
    return Block(0, datetime.datetime.now(), 'Genesis!!', '0')

def next_block(prev_block, block_data):
    block_index = prev_block.index + 1
    block_timestamp = datetime.datetime.now()
    block_hash = prev_block.hash
    return Block(block_index, block_timestamp, block_data, block_hash)

blockchain = [create_genesis_block()]
prev_block = blockchain[0]
print('nonce : ' + str(blockchain[0].nonce))
print('data : ' + blockchain[0].data)
print('hash : ' + blockchain[0].hash)
print('prev : ' + blockchain[0].prev, '\n')

new_block = next_block(prev_block, '2nd')
new_block.hash, new_block.nonce = proof_of_work(new_block)
blockchain.append(new_block)
prev_block = new_block

print('nonce : ' + str(blockchain[1].nonce))
print('data : ' + blockchain[1].data)
print('hash : ' + blockchain[1].hash)
print('prev : ' + blockchain[1].prev, '\n')

new_block = next_block(prev_block, '3rd')
new_block.hash, new_block.nonce = proof_of_work(new_block)
blockchain.append(new_block)
prev_block = new_block

print('nonce : ' + str(blockchain[2].nonce))
print('data : ' + blockchain[2].data)
print('hash : ' + blockchain[2].hash)
print('prev : ' + blockchain[2].prev, '\n')