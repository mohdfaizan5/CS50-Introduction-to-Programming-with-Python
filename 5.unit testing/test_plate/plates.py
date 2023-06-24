def main():
    ...
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    ...
    #Step1: Max 6 charators and min of 2 charactors
    leng = len(s)
    # print(leng)
    if leng < 2 or leng > 6:
        # print("invalid leng")
        return False

#step2 : no period or spaces or puncuation should be used
    for c in s:
        if c == "," or c == " " or c == ".":
            # print("period is used")
            return False


#Step2 : Starting 2 charactors should be (alphabets)
    first_2_char = s[0:2]
    # sec_2_char = s[2:5]
    if not first_2_char.isalpha(): #??? Why am I not able to use functions over here
        # print("First 2 letters should be alphabets")
        return False
    # if s[-1:-3]

    # print(type(s))

#Step3 : No. cannot be in middle of plate(nos. should only be in the end) and
    # last_letter = s[-1]
    # if last_letter isalpha():
    #     print("middle should not be number.")



    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be
    # an acceptable … vanity plate; AAA22A would not be acceptable.

    index = 0
    for char in s:
        if char.isnumeric():
            for i in s[index:]:
                if i.isalpha():
                    return False

        index += 1

    len_s = len(s)
    if len_s > 3:
        if s[2] == "0":
            # print("3rd char should not start with 0")
            return False



    # f = s[0:2]
    # print(f)
    return True


if __name__ == "__main__":
    main()