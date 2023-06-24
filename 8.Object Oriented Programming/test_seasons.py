from seasons import convert

def test_my_date1():
    assert convert("2001-01-01") == "Eleven million, six hundred forty-nine thousand, six hundred minutes"

def test_my_birthday():
    assert convert("2003-12-13") == "Ten million, one hundred thousand, one hundred sixty minutes"

def test_2():
    assert convert("2001-01-01") == "Eleven million, six hundred forty-nine thousand, six hundred minutes"

def test_3():
    assert convert("2020-06-01") == "One million, four hundred thirty-eight thousand, five hundred sixty minutes"