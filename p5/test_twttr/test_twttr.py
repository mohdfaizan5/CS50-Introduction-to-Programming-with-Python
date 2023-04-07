from twttr import shorten

# twttr.shorten("faizan")
def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("faizan") == "fzn"
    assert shorten("test") == "tst"
    # return 0
    # print("worked lower")


def test_uppercase():
    assert shorten("FAIzAN") == "FzN"
    assert shorten("tEST") == "tST"
#     print("worked upper")
    # return 0

def test_numb():
    assert shorten("FAIzAN1") == "FzN1"
    assert shorten("3tEST") == "3tST"
#     print("worked upper")
    # return 0
def test_punc():
    assert shorten(".FAIzAN1") == ".FzN1"
    assert shorten("1.twitter") == "1.twttr"


# if __name__ == "__main__":
#     test_shorten()
#     test_uppercase()

# pygobject 3.36.0 requires pycairo, which is not installed.
# launchpadlib 1.10.13 requires testresources, which is not installed.
# lib50 3.0.4 has requirement termcolor<2,>=1.1, but you have termcolor 2.1.1.