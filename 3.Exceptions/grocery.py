#Program for grocery list noting:
# import keyboard
import pdb
#S1: Prompt user for input, one per line
#S2: Stops when the user inputs control-d
#S3: Then output the user’s grocery list in all uppercase, sorted alphabetically by item
#S4: prefixing each line with the number of times the user inputted that item

all_items = {}
user_items = []



def count_items(all_items):
    user_items.sort()
    
    for item in user_items:
        if item not in all_items:
            all_items[item] = 1

        else:
            all_items[item] += 1
    


def main(all_items, user_items): #=all_items, user_items=user_items):
    # i = 0
    while True:
        items = input("").upper()
        user_items.append(items)
        
        # pdb.set_trace()
        # if i == 4:
        #     return all_items,items
# all_items.


try:
    main(all_items,user_items)
except EOFError:
    count_items(all_items=all_items)
    # print("EOF error")
    # print(f"final: {all_items}")
    for _ in all_items:
        i = 0
        print(f"{all_items[_]} {_}")
        i += 1
# else:
    # all_items.
    
#Doubt and issue
# D1: how to print particular key for that 
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""