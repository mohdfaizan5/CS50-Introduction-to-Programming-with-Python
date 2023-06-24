from um import count

def main1():
    upper_cases()
    lower_cases()
    with_chars()

def upper_cases():
    assert count("Um") == 1

def lower_cases():
    assert count("um, thats yummy") == 1

def with_chars():
    assert count("hello  world") == 0
    assert count("Um, thanks for the album.") == 1

if __name__ == "__main__":
    main1()