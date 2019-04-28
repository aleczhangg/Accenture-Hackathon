import threading
import time
import random
import sys


class PeriodicCommit(threading.Thread):
    def __init__(self, bc):
        super(PeriodicCommit, self).__init__()
        self.blockchain = bc

    def run(self):
        while True:
            nonce = random.randint(0, sys.maxsize)
            if self.blockchain.commit(nonce):
                print(self.blockchain)
            time.sleep(0.05)