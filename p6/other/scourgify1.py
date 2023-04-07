#PROGRAM THAT REFORMATES THE DATA OF GIVEN CSV FILE:
import os, sys, csv, pdb
# sys.argv = [os.path.basename(__file__),(r"C:\Users\knightrider5\Desktop\Python\CS50p\6.files\other\before.csv"), (r"C:\Users\knightrider5\Desktop\Python\CS50p\6.files\other\after.csv")]

def check_valid():

    # S1: Expects exactly one command-line argument, the name (or path) of a Python file
    # S2: If the user does not specify exactly one command-line argument, or if the specified
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    file_name = str(file_name)

    # S2: If file’s name does not end in .py, or if the specified file does not exist,
                                    # the program should instead exit via sys.exit.
    if not file_name.endswith(".csv"):
        sys.exit(f"Could not read {file_name}")
    #for checking if file exists
    with open(file_name) as file:
        file_name = file_name
    return file_name

def main(file_name=sys.argv[1]):
    data = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            first, last = (row["name"]).split(",")
            data.append({"first":first.lstrip(),"last":last.strip(),"house":row["house"].strip()})
        with open(sys.argv[-1],"w") as file:
            writer = csv.DictWriter(file,fieldnames=["first","last","house"])
            writer.writerow({"first":"first","last":"last","house":"house"})
            for row in data:
                writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})

try:
    check_valid()
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()