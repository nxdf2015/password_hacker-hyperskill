from sys import argv
from  socket import socket



# Create a new socket.
# Connect to a host and a port using the socket.
# Send a message from the third command line argument to the host using the socket.
# Receive the server’s response.
# Print the server’s response.
# Close the socket.

domain,port,message = argv[1:]

address =( domain, int(port))


with socket() as  client:
    client.connect(address)
    client.send(message.encode())
    size_buffer = 1024
    response = client.recv(size_buffer)
    print(response.decode())



