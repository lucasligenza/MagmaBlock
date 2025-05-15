import time
import hashlib
import json

class Block:
    def __init__(self, index, previous_hash, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.data = data
        self.nonce = nonce

    def compute_hash(self):
        """
        Return the SHA-256 hash of this block’s header.
        You need to:
          1. Serialize the header fields in a deterministic order.
          2. Feed the bytes into hashlib.sha256().
          3. Return the hex digest.
        """

        # Pack the header fields into a dict
        block_header = {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'nonce': self.nonce,
        }

        # Serialize the header fields in a deterministic order
        header_string = json.dumps(block_header, sort_keys=True)

        # Compute the SHA-256 hash
        hash_bytes = hashlib.sha256(header_string.encode())

        # Return the hex digest
        return hash_bytes.hexdigest()

if __name__ == "__main__":
    # Make a test block
    b = Block(index=1, previous_hash="0"*64, data="My first block")
    
    # Compute its hash
    h1 = b.compute_hash()

    # Test nonce differences
    b.nonce = 0

    # Compute its hash again
    h2 = b.compute_hash()
    
    print("Hash 1:", h1)
    print("Hash 2:", h2)
    print("Same both times?", h1 == h2)
