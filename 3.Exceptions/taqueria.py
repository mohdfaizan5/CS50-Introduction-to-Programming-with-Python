#implement a program that enables a user to place an order

import sys
import keyboard
# import 
readkey = keyboard.read_key()
print(readkey)
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
                print(f"Total: ${total_amt}") #, end ="\n"
            
            if keyboard.read_key() == "a":
                print("You pressed 'a'.")
                break
    except EOFError:
        return True
        print("ctrl d")
    else:
        sys.exit()
    # except EOFError as e:
    #     print(e)
    # elif KeyboardInterrupt:
# elif 

    
    
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


#Doubts
"""
1. How to exit program when ctrl + D is hit
2.  modules keyboard (modules which are installed from pip are not working)
3. Check50 program is not working


check50 cs50/problems/2022/python/taqueria
"""