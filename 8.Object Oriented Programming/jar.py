# PROGRAM TO STORE COOKIES

class Jar:
    def __init__(self, capacity=12):

        # __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of
        # cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should
        # instead raise a ValueError.
        self._capacity = capacity
        self._size = 0


    def __str__(self):

        # __str__ should return a str with \(n\) 🍪, where \(n\) is the number of cookies in the cookie jar.
        # For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        return self._size * "🍪"

    def deposit(self, n):

        # deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
        # though, deposit should instead raise a ValueError.
        if self._size + n > self._capacity or n > self._capacity:
            raise ValueError("Can't add cookies more than the capacity")
        self._size += n

    def withdraw(self, n):

        # withdraw should remove n cookies from the cookie jar. If there aren’t that many cookies in
        # the cookie jar, though, withdraw should instead raise a ValueError.
        if n > self._size:
            raise ValueError("we don't have enough cookies to remove")
        self._size -= n

    @property
    def capacity(self):

        # capacity should return the cookie jar’s capacity.
        return self._capacity

    # @capacity.setter
    # def _capacity(self, _capacity):
    #     if self._capacity <= 0:
    #         raise ValueError("capacity cant be lesser than 1")

    @property
    def size(self):
        # size should return the number of cookies actually in the cookie jar.
        return self._size

# jar = Jar(1)
# jar1 = Jar(-1)