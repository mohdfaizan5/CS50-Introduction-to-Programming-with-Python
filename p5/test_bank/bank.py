import pdb

def main():
    ...
    greeting = input("Greeting: ").lower().strip()
    value(greeting)

def value(greeting):
    ...
    #returns 0 if that str starts with “hello”, 20 if that str starts
    # with an “h” (but not “hello”), or 100 otherwise
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        # print("$0")
        return 100
    elif greeting.startswith("h"):  #and greeting != "hello": #or greet != "hello ":
        # print("$20")              #👆 (we don't need this as up condition has already checked for this)
        # pdb.set_trace()
        return 20
    else:
        return 0

if __name__ == "__main__":
    main()