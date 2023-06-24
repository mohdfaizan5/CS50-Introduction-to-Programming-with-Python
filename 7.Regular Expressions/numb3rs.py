#PROGRAM THAT VALIDATES IP ADRESS ""
import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if lists := re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        lists = ip.split(".")
        # print(lists)
        for num in lists:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
