from numb3rs import validate

def main():
    test_format()
    test_value()

def test_format():
    assert validate("cat.dog") == False
    assert validate("1.1..1.1") == False
    assert validate("127.0.0.1") == True


def test_value():
    assert validate("0.0.0.0") == True
    assert validate("0.1.1.256") == False
    assert validate("255.255.255.255") == True

if __name__ == "__main__":
    main()