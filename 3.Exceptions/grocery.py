#Program for grocery list noting:
import pdb
#S1: Prompt user for input, one per line
#S2: Stops when the user inputs control-d
#S3: Then output the user’s grocery list in all uppercase, sorted alphabetically by item
#S4: prefixing each line with the number of times the user inputted that item

list = {}
def main(list):
    try:
        while True:
            items = input("")
            list = list[items]
            pdb.set_trace()
            print(list)
    except:
        print("error")
        
        
main(list)