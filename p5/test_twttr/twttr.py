#Problem that takes input from user and eliminates the vovels "a,e,i,o,u"

def main():
    usr_input = input("Input: ")
    shorten(usr_input)
    print(f"Output: {shorten()}")

def shorten(usr_input):
    #shorten expects a str as input and returns that same str but with all vowels
    # (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

    vowels = ["a", "e", "i","o","u"]#,"A","E","I","O","U"]
    for vowel in vowels:
        usr_input = usr_input.replace(vowel,"")
    return usr_input

if __name__ == "__main__":
    main()



    """
:) test_twttr.py exist
:) correct twttr.py passes all test_twttr checks
:) test_twttr catches twttr.py without vowel replacement
:( test_twttr catches twttr.py without capitalized vowel replacement
    expected exit code 1, not 0
        #for this i eliminated the part of code that replaces CAP LETTERS

:) test_twttr catches twttr.py without lowercase vowel replacement
:( test_twttr catches twttr.py omitting numbers
    expected exit code 1, not 0
:) test_twttr catches twttr.py printing in uppercase
:( test_twttr catches twttr.py omitting punctuation
    expected exit code 1, not 0
    """