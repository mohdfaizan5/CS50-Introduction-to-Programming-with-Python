import os
print("global print")
def main_sample():
    print("inside main of sample")
    
print("Printing attributes of sample.py")
print(dir())
if __name__ == "__main__":
    print("if passed, calling main of sample.py")
    main_sample()
else:
    print("inside else of sample.py")