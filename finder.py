from abc import abstractmethod
from string import ascii_lowercase
from itertools import product,combinations
from functools import reduce
from operator import add


class Finder:

    @abstractmethod
    def find_password(self):
        pass



class AlphabeticPassword(Finder):
    """
        generate all passwords with lowercase letters and numbers 0 to 9
    """
    def find_password(self):

        letters = ascii_lowercase + "0123456789"
        generator = letters
        while True:
            for word in generator:
                yield tuple_to_string(word)
            generator = product(letters,generator)



class DictionnaryPassword(Finder):
    """
     Use the dictionary of standard passwords changing the cases of different letters
    """
    def __init__(self,namefile):
        self.namefile=namefile

    def find_password(self):
        with open(self.namefile) as f:
            for password in f.readlines():

                try:
                    int(password)
                    yield  password
                    continue
                except:
                    password=list(password.strip())
                    size = len(password)
                    for i in range(size):
                        for c in combinations(range(size),i):
                            copy=password[:]
                            for j in c:
                                copy[j] = copy[j].upper()
                            yield "".join(copy)



def tuple_to_string(word):
    return reduce(add,word,"")

