from plates import is_valid

# four or more test or functions here


def test_startchars():
    assert is_valid("TE") == True
    assert is_valid("CS50") == True
    assert is_valid("N2") == False
    assert is_valid("4GREATer") == False
#Testing for length

def test_len():
    assert is_valid("CS") == True
    assert is_valid("Faizna1") == False
    assert is_valid("Helo") == True
    assert is_valid("") == False
    # print("len passed")

#Testing period, puncuation. whitespace
def test_specialChar():
    assert is_valid("CS,") == False
    assert is_valid("Fai zna1") == False
    assert is_valid("Fai.") == False
    assert is_valid("Fai12") == True
    # print("Special chars passed")

#Testing starting 2 char are alphabets
def test_isalpha():
    assert is_valid(",CS") == False
    assert is_valid("F1izna1") == False
    assert is_valid("F. aizna1") == False
    assert is_valid("CS50") == True
    # print("first 2 char are alpha passed")

# Testing “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be
# an acceptable … vanity plate; AAA22A would not be acceptable.
def test_middle_char():
    assert is_valid("CS50P") == False
    assert is_valid("Fa03") == False
    assert is_valid("aS10") == True
    assert is_valid("FMe3") == True
    # print("no. not in middle passed")


# if __name__ == "__main__":
#     test_len()
#     test_isalpha()
#     test_specialChar()
#     test_middle_char()
#     test_startchars()

"""
:) test_plates.py exist
:) correct plates.py passes all test_plates checks
:( test_plates catches plates.py without beginning alphabetical checks
    expected exit code 1, not 0
:( test_plates catches plates.py without length checks
    expected exit code 1, not 0
:) test_plates catches plates.py without checks for number placement
:) test_plates catches plates.py without checks for zero placement
:) test_plates catches plates.py without checks for alphanumeric characters
"""