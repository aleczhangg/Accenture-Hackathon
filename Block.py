import hashlib


class Block:
    def __init__(self, pool):
        self.previous_block = None
        self.previous_hash = 0
        self.pool = pool

    def __repr__(self):
        dashes = "-" * 50 + "\n"
        string = dashes + "Block Hash: " + self.calculate_hash() + "\n" + dashes

        for ticket in self.pool:
            string += repr(ticket)

        return string + dashes

    # Use SHA-256 to return a hash of the block.
    def calculate_hash(self, nonce=None):
        hashable_string = str(self.previous_hash)
        for entry in self.pool:
            hashable_string += entry.hashable()
        if nonce is not None:
            hashable_string += str(nonce)
        return hashlib.sha256(hashable_string.encode()).hexdigest()

