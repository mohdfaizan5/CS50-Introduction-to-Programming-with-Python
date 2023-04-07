#PROGRAM THAT FIND THE FILLER WORD "um" IN GIVEN TEXT:

import re


def main():
    print(count(input("Text: ").lower()))

def count(s):
    pattern = re.findall(r"\b(um)\b",s,re.IGNORECASE)
    return len(pattern)

if __name__ == "__main__":
    main()