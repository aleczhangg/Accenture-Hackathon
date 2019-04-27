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
            time.sleep(0.05)

if __name__ == "__main__":
    print("Starting up periodic commit.")
    # Instantiate a blockchain.
    blockchain = Blockchain()
    # Start adding already existing tickets.
    blockchain.add_og_ticket("Ticketek")
    blockchain.add_og_ticket("Ticketek")
    blockchain.add_og_ticket("Ticketek")
    blockchain.add_og_ticket("Ticketek")

    thread_commit = PeriodicCommit(blockchain)
    thread_commit.start()

    while True:
        prompt = input("What do you want to do?\n").split()

        if prompt[0] == "exit":
            print("Goodbye.")
            thread_commit.join(0.5)
            break
        elif prompt[0] == "print":
            print(blockchain)
        elif prompt[0] == "find":
            tid = prompt[1]
            print(blockchain.find_owner(tid))
        elif prompt[0] == "transfer":
            blockchain.transfer_ticket(prompt[1], prompt[2], prompt[3], prompt[4])
        elif prompt[0] == "head":
            print(blockchain.head)
        else:
            print("Unknown command.")

    # block = Block([Entry("Michelle"), Entry("Jerry")])
    # print(block)


