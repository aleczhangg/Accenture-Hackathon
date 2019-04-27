from Block import Block
from Entry import Entry
from Blockchain import Blockchain
import random
import threading
import sys
import time


class PeriodicCommit(threading.Thread):
    def __init__(self, bc):
        super(PeriodicCommit, self).__init__()
        self.blockchain = bc

    def run(self):
        while True:
            nonce = random.randint(0, sys.maxsize)
            if self.blockchain.commit(nonce):
                print(self.blockchain)
            time.sleep(0.5)


class UserInput(threading.Thread):
    def __init__(self, bc):
        super(UserInput, self).__init__()
        self.blockchain = bc

    def run(self):
        while True:
            user_input = input()
            if user_input == "exit":
                break
            elif user_input == "help":
                print("lmao")
            else:
                self.blockchain.add_entry(Entry(user_input))


if __name__ == "__main__":
    print("Starting up periodic commit.")
    blockchain = Blockchain()
    thread_commit = PeriodicCommit(blockchain)
    thread_user = UserInput(blockchain)
    thread_commit.start()
    thread_user.start()

    # block = Block([Entry("Michelle"), Entry("Jerry")])
    # print(block)


