#Program that takes user names and prints it adding "adieu" and comma
#Program that takes name and add "and" and "and," or ","

#STEP1: takes input from user

#Program that takes name and add "and" and "and," or ","

import inflect
p = inflect.engine()
#Creating a list comprehension
names = []

#STEP1: takes input from user
while True:
    try:
        user_name = input("Name: ")
        names.append(user_name)
    except EOFError:
        # print()
        break

#Step3: Printing the output
s = p.join(names)
print(f"Adieu, adieu, to {s}")