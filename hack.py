from sys import argv,path
import sys
path += ["C:\\Users\\nique\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking"]
from client import Client, ClientLogin
from finder import DictionnaryPassword,AlphabeticPassword





def main():
    domain,port = argv[1:]
    address =( domain, int(port))
    filename = ".\\hacking\\passwords.txt"
    # with Client(address) as client:
    #     #password.search(AlphabeticPassword())
    #     client.set_finder( DictionnaryPassword(filename))
    #     client.search()

    with ClientLogin(address) as client:
        client.search()



main()


