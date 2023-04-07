#program that shorten the html youtube link and returns the simplified link

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # s1 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    # s2 = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    # if pattern := re.search(r"^(<ifram).+(</iframe>)",s2):
    if pattern := re.search(r'^(?:<iframe).* src="http[s|]://(?:www.)?you(.*?)"',s):
        a = pattern.group(1).split("/")
        a = a[-1]
        a = str(a)
        return ("https://youtu.be/"+a)

if __name__ == "__main__":
    main()