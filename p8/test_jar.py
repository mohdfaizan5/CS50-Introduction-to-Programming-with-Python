
from jar import Jar


def test_init():
    # Test default initialization
    jar = Jar()
    assert jar.capacity == 12

    # Test custom value initializations
    jar1 = Jar(1)
    assert jar1.capacity == 1


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():

    # Testing deposit by adding 1
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

    jar.deposit(2)
    assert jar.size == 3

def test_withdraw():

    j = Jar()
    j.deposit(11)
    j.withdraw(1)
    assert j.size == 10

    j.withdraw(5)
    assert j.size == 5