from Block import Block
from Ticket import Ticket
import random


def random_word():
    file = open("words.txt", 'r')
    words = file.readlines()
    choice = ""
    while len(choice) < 3:
        choice = random.choice(words)
        choice = choice.capitalize()
    return choice.strip("\n")


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

    def find_prev_ticket(self, tid):
        block = self.head
        while block is not None:
            for ticket in block.pool:
                if ticket.tid == tid:
                    return ticket
            block = block.previous_block
        return None

    def find_owner(self, tid):
        block = self.head
        while block is not None:
            for ticket in block.pool:
                if ticket.tid == tid:
                    return ticket.person
            block = block.previous_block

    def add_og_ticket(self, owner):
        ticket = Ticket("source", owner, 0)
        ticket.tid = random_word()
        self.pool.append(ticket)

    def transfer_ticket(self, tid, old_owner, new_owner, price):
        # Find the previous transaction involving this ticket id.
        prev_ticket = self.find_prev_ticket(tid)
        # If this previous transaction is not found, return an error.
        if prev_ticket is None:
            print("Failed: Ticket is not owned by {}.".format(old_owner))
        # If it is found, do the transfer.
        else:
            new_ticket = Ticket(old_owner, new_owner, price)
            new_ticket.tid = tid
            new_ticket.resale_count = prev_ticket.resale_count + 1
            self.pool.append(new_ticket)
            print("Successful.")


