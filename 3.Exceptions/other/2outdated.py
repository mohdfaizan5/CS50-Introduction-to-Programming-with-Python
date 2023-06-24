


import sys
# import keyboard
# import
# readkey = keyboard.read_key()

# print(readkey)
# imp
total_amt = 0
#S1: Prompting them for "Item: " one per line {Assume that every item on the menu will be titlecased.}
def main(total_amt):
    try:
        while True:
            order = input("Item: ").title()
            if order in menu:
                # print(f"{menu[order]} yes")
                total_amt += menu[order]
                total_amt = float(total_amt)
                print(f"Total: ${total_amt.__round__(2)}") #, end ="\n"

            # if keyboard.read_key() == "a":
            #     print("You pressed 'a'.")
            #     break
    except EOFError:
        return True
        # print("ctrl d")
    else:
        sys.exit()



#S2: Show the user the total cost of his order(display the total cost of all items inputted thus far) prefixed with a dollar sign ($) and formatted to two decimal places
#S3: until the user inputs control-d (which is a common way of ending one’s input to a program).
# After each inputted item, ,. Treat the user’s input case insensitively.
# Ignore any input that isn’t an item.


menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main(total_amt)



# import pdb
# import sys
# user_input = input("Date: ")

# MONTHS = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# #S : Take input from user.


# def method1(x = user_input):
#     x = x.split("/")
#     if int(x[1]) > 31:
#         sys.exit()
#         print("date exceed")
#     print(f"{x[2]}-{x[0].zfill(2)}-{x[1].zfill(2)}")
#     #:02d}-{x[1]:02d}")
#     # {i:02d}


# def method2(z = user_input):
#     z = z.replace(",","")
#     z = z.split()
#     mo = int(z[1])
#     m1 = 31


#     if mo > m1:
#         sys.exit()
#     month = z[0]    #December
#     # i = 0
#     index = 1
#     for _ in MONTHS:
#         if month == _:
#             z[0] = index # 12
#             print(month)
#         index += 1

#     print(f"{z[2]}-{z[0]}-{z[1]}")


# try:
#     # while True:
#         # converting(user_input)
#     if user_input[0].isnumeric():
#         #If its only date then method1
#         method1()

#     else:
#         #method..
#         method2()


# except IndexError:
#     print("error")