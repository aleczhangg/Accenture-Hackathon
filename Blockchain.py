from Block import Block


class Blockchain:
    def __init__(self):
        self.head = None  # Most recent block in the blockchain.
        self.pool = []  # Stores entries waiting to be committed.
        self.length = 0  # How many blocks are in the blockchain.

    def __repr__(self):
        string = "Start of blockchain.\n"

        block = self.head
        while block is not None:
            string += repr(block)
            block = block.previous_block

        return string

    def add_entry(self, entry):
        self.pool.append(entry)

    def commit(self, nonce):
        # If there are no entries to be committed, just ignore this.
        if len(self.pool) == 0:
            return
        else:
            # Try creating a new block to store the entries.
            new_block = Block(self.pool.copy())
            new_block.previous_block = self.head
            if self.head is not None:
                new_block.previous_hash = self.head.calculate_hash()
            else:
                new_block.previous_hash = 0

            # Check the hash of this new block, then commit.
            hash_value = new_block.calculate_hash(nonce)
            if hash_value[0] == "a":
                self.head = new_block
                self.pool = []
                self.length += 1
                print("New block committed!")
                return True






