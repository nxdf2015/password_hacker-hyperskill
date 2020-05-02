from sys import argv,path
import sys

from client import Client
from finder import DictionnaryPassword,AlphabeticPassword


domain,port = argv[1:]
address =( domain, int(port))
filename = ".\\hacking\\passwords.txt"

def main():
    with Client(address) as client:
        #password.set_finder(AlphabeticPassword())
        client.set_finder( DictionnaryPassword(filename))
        client.search()


main()





