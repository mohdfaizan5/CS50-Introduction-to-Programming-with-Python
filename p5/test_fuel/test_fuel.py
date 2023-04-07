from fuel import convert,gauge
import pytest

def main():
    test_input()
    test_zero_division_error()
    test_value_error()

def test_input():
    assert convert("99/100") == 99 and gauge(99) == "F"
    # a = convert("3/4")
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    # assert gauge(99/100) == "F"


# def test_gauge():
#     assert gauge("100") == "F"
#     assert gauge(75) == "75%"


def test_zero_division_error():
    # assert convert("4/0") != ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("thre/four")

if __name__ == "__main__":
    main()