from sys import argv,path
import sys

from client import Client
from finder import DictionnaryPassword,AlphabeticPassword


domain,port = argv[1:]
address =( domain, int(port))
filename = ".\\hacking\\passwords.txt"

def main():
    with Client(address) as password:
        #password.set_finder(AlphabeticPassword())
        password.set_finder( DictionnaryPassword(filename))
        password.search()


main()





