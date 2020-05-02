from socket import socket


class Client:
    size_buffer = 1024

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

