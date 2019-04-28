# Accenture Hackathon: Team 7
### Main Ideas
Our project deals with the issue of ticket fraud: namely the selling of duplicate copies, and the selling of counterfeit copies of say concert tickets. Our solution implements a blockchain ledger system that keeps track of exchanges of these tickets, and is done through *a blockchain server* and an *iOS client* that interfaces with the server.

### Blockchain Server
The most important file is BlockchainServer.py, run this in Terminal and it should set up a server at localhost:8000.

Block.py and Blockchain.py are the basic classes that we have used to implement a blockchain. Our blockchain is implemented as a linked list, where our proof of working comes from a multithreaded server that attempts to guess a hash for a block that starts with "a" using the PeriodicCommit.py class.

Ticket.py provides the structure of the *transactions* that we are storing in the blockchain ledger.

### iOS Client
The iOS client requires the dependency manager CocoaPods - we have used the open source library SwiftSocket to enable for our client-server interactions. Documentation for this is available at https://github.com/swiftsocket/SwiftSocket

The app is best run using an iPhone 8 Plus.
