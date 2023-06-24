# PROGRAM TO STORE COOKIES
import pdb

class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity # IT IS A INSTANCE VARIABLE
        self.size = 0
        # __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of
        # cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should
        # instead raise a ValueError.

    def __str__(self):
        # __str__ should return a str with \(n\) 🍪, where \(n\) is the number of cookies in the cookie jar.
        # For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        return self.size * "🍪"

    def deposit(self, n):

        # deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
        # though, deposit should instead raise a ValueError.
        if n > self.capacity:
            raise ValueError("you cant insert more cookies than capacity of jar")
        if self.size + n > self.capacity:
            raise ValueError("your over filling the jar with cookies")
        self.size += n




    def withdraw(self, n):

        # withdraw should remove n cookies from the cookie jar. If there aren’t that many cookies in
        # the cookie jar, though, withdraw should instead raise a ValueError.

        if n > self.size:
            raise ValueError("don't have that much value cookies to remove")

        self.size -= n


    # Getter function
    @property
    def capacity(self):
        return self._capacity
    #     # capacity should return the cookie jar’s capacity.


    # Setter function
    @capacity.setter
    def _capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("hi hello")
        self._capacity = capacity



    @property
    def size(self):
    #     # size should return the number of cookies actually in the cookie jar.
        return self.size

    # @property
    # def deposit(self):
    #     return self._deposit

    # @deposit.setter
    # def deposit(self, deposit):
    #     if deposit >


jar1 = Jar(1)
print(jar1.capacity)
pdb.set_trace()