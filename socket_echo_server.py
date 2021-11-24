import socket as sc 
import sys

# Create a TCP/IP socket
sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
host = "" # the ip you gonne use to host the server
port = 2000 # the port your server is going to Listen

# Bind the socket to the port
server_address = (host, port)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()