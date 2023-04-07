from um import count

def test_upper_cases():
    assert count("Um") == 1
    assert count("um ") == 1


def test_lower_cases():
    assert count("um, thats yummy") == 1
    assert count("yummy") == 0



def test_with_chars():
    assert count("hello  world") == 0
    assert count("Um, thanks for the album.") == 1
