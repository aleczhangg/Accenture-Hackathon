import threading
import time
import random
import sys


# Runs as a thread in the blockchain server.
class PeriodicCommit(threading.Thread):
    def __init__(self, bc):
        super(PeriodicCommit, self).__init__()
        self.blockchain = bc

    # Thread continually tries to guess a hash for the block following a rule.
    def run(self):
        while True:
            nonce = random.randint(0, sys.maxsize)
            if self.blockchain.commit(nonce):
                print(self.blockchain)
            time.sleep(0.05)