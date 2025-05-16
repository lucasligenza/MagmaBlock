from block import Block

class Blockchain:
    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Make sure the genesis block is created only once
        if self.chain:
            return
        
        # Create the first block
        genesis = Block(index=0, previous_hash="0"*64, data="Genesis Block")

        # Compute the hash of the genesis block
        genesis.hash = genesis.compute_hash()

        # Append to the chain
        self.chain.append(genesis)

    def get_last_block(self):
        # Return the last block in the chain
        return self.chain[-1] if self.chain else None
    
    def add_block(self, data, difficulty=2):
        # Use info from the last block to create a new one
        last_block = self.get_last_block()
        new_index = last_block.index + 1
        
        # Build the block
        new_block = Block(index=new_index,
                          previous_hash=last_block.hash,
                          data=data)
        
        # Mine the block (find a valid nonce)
        new_block.mine(difficulty)
        
        # Add it onto our chain
        self.chain.append(new_block)

    def is_valid(self):
        # Check if the blockchain is valid
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check if the hash of the current block is correct
            if current.hash != current.compute_hash():
                return False

            # Check if the previous hash of the current block matches the hash of the previous block
            if current.previous_hash != previous.hash:
                return False

        return True

if __name__ == "__main__":
    bc = Blockchain()
    # Mine two blocks with “2 zeros” difficulty
    bc.add_block("Block 1 data", difficulty=2)
    bc.add_block("Block 2 data", difficulty=2)

    for block in bc.chain:
        print(f"#{block.index} | nonce={block.nonce} | hash={block.hash[:8]}…")

