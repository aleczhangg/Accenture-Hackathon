from Blockchain import Blockchain
from PeriodicCommit import PeriodicCommit
import socket

# Server handler that deals with user data.
def server_handler(data, client):
    prompt = data.split("|")
    if prompt[0] == "print":
        message = repr(blockchain)
        client.sendall(message.encode())
        return
    if prompt[0] == "exit":
        message = "\nGoodbye.\n"
        client.sendall(message.encode())
        return -1
    elif prompt[0] == "print":
        message = "\n" + repr(blockchain) + "\n"
        client.sendall(message.encode())
    elif prompt[0] == "find":
        tid = prompt[1]
        message = "Ticket {} is owned by {}.\n\n".format(tid, blockchain.find_owner(tid))
        client.sendall(message.encode())
    elif prompt[0] == "transfer":
        print("Transfer request received.")
        if len(prompt) != 5:
            message = "-1"
            client.sendall(message.encode())
            return "Successful transfer."
        success = blockchain.transfer_ticket(prompt[1], prompt[2], prompt[3], prompt[4])
        print("Transfer value:" + success)
        client.sendall(success.encode())
    elif prompt[0] == "owner":
        tickets = blockchain.find_owned_tickets(prompt[1].rstrip())
        message = ""
        for ticket in tickets:
            message += ticket.to_client()
        print("Owned tickets found successfully.")
        client.sendall(message.encode())
    else:
        message = "Unknown command.\n\n"
        client.sendall(message.encode())


if __name__ == "__main__":
    # Set up the blockchain and commits first.
    blockchain = Blockchain()
    # Start adding already existing tickets.
    blockchain.add_og_ticket("Alec")
    blockchain.add_og_ticket("Jerry")
    blockchain.add_og_ticket("Tiger")

    # Start a thread that continually tries to commit.
    thread_commit = PeriodicCommit(blockchain)
    thread_commit.start()

    # Set up the server.
    HOST = "localhost"
    PORT = 8000

    # Create a server socket to listen for clients.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    try:
                        data = conn.recv(1024*10)
                        if not data:
                            break
                        if data:
                            ret = server_handler(data.decode("utf-8"), conn)
                            print(ret)
                    except Exception:
                        break
                conn.close()
