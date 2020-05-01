from sys import argv
from  socket import socket
from string import ascii_lowercase
from itertools import product
from functools import reduce
from operator import add

# Create a new socket.
# Connect to a host and a port using the socket.
# Tries different passwords until it finds the correct one.
# Prints the password it found. when the server response is 'Connection success!"
# Close the socket.


domain,port = argv[1:]
address =( domain, int(port))

def tuple_to_string(word):
    return reduce(add,word,"")

def find_password():
    """
     generate all passwords with lowercase letters and numbers 0 to 9
    """
    letters = ascii_lowercase + "0123456789"
    generator = letters
    while True:
        for word in generator:
            yield tuple_to_string(word)
        generator = product(letters,generator)




with socket() as  client:
    client.connect(address)
    size_buffer = 1024
    for password in find_password():
        client.send(password.encode())
        response = client.recv(size_buffer).decode()
        if response == "Connection success!":
            print(password)
            break






