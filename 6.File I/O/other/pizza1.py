#expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table
# formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
# Format the table using the library’s grid format. If the user does not specify exactly
# one command-line argument, or if the specified file’s name does not end in .csv, or if
# the specified file does not exist, the program should instead exit via sys.exit.
import csv,sys,pdb
from tabulate import tabulate

##S1: Take input from user
lines = []
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
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    return file_name

try:
    with open(check_valid()) as file:
        # reader = csv.reader(file)   #Reader just reads the data of the file and stores in it.
        # for _ in reader:
        #     lines.append(_)
        reader = csv.DictReader(file)
        print(tabulate(reader,headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
