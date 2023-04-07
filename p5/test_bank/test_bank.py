from bank import value

def test_value():
    assert value("hello") == 0
    assert value("heello") == 20
    assert value("d") == 100
    # print("worked")

def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    # print("passed 0")

def test_20():
    assert value("heello") == 20
    assert value("Hi") == 20
    assert value("HEadache") == 20
    # print("passed 20")


def test_100():
    assert value("faizan") == 100
    assert value("your are awesome") == 100
    assert value("StomaChAche") == 100
    # print("passed 100")

if __name__ == "__main__":
    test_value()
    test_0()
    test_20()
    test_100()


# """
# ) test_bank.py exist
# :( correct bank.py passes all test_bank checks
#     expected exit code 0, not 2
# :| test_bank catches bank.py with incorrect values
#     can't check until a frown turns upside down
# :| test_bank catches bank.py without case-insensitivity
#     can't check until a frown turns upside down
# :| test_bank catches bank.py not allowing for entire phrase
#     can't check until a frown turns upside down
# """



# import sys

# if sys.argv[1] == "fa":
#     print("ok")
# else:
#     print("not working")
