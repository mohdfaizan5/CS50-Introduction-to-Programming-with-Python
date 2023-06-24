# PROGRAM THE COUNTS NO. OF LINES IN A PYTHON FILE EXCLUDING (COMMENTS AND BLACK LINES)
import sys,os

# sys.argv = [os.path.basename(__file__),(r"C:\Users\knightrider5\Desktop\Python\CS50p\6.files\pizza.py")]
            #specifing the file name   #first argument
# print(sys.argv[0],sys.argv[1])
# print(len(sys.argv))

def check_valid():

    # S1: Expects exactly one command-line argument, the name (or path) of a Python file
    # S2: If the user does not specify exactly one command-line argument, or if the specified

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file_name = sys.argv[1]

    # S3: If file’s name does not end in .py, or if the specified file does not exist,
                                    # the program should instead exit via sys.exit.
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")
    return file_name

def main(file_name):
# S4: outputs the number of lines of code in that file, excluding comments and blank lines.
    no_of_lines = 0
    with open(file_name) as file:
        lines = file.readlines()
        # print(lines)
        for line in lines:
            if check_code(line):
                no_of_lines += 1

    print(f"Lines = {no_of_lines}")



def check_code(line):
    # if not line.isspace() or not line.startswith("#"):
    #     no_of_lines += 1
    # if not line.isspace():
    #     no_of_lines += 1``
    if line.isspace():
        return False
    if line.lstrip().startswith("#"):
        return False
    return True
    # elif not line.startswith("#"):
    #     no_of_lines += 1

try:
    main(check_valid())
except FileNotFoundError:
    sys.exit("File does not exist")



#Note:
    #Assume that any line that starts with #, optionally preceded by whitespace,
    #  is a comment. (A docstring should not be considered a comment.)
    # Assume that any line that only contains whitespace is blank.


### TO-DO

    # [ ] Watch video lecture files in 1.4x speed and takes notes
    # [ ] Make proper notes.
    # [ ]

# file_name  = "pizza.py"

# a = open(file_name,'r')
# print(a)
