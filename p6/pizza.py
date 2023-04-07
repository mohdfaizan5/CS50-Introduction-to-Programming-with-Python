import sys,pdb,csv
from tabulate import tabulate


def main():
    check_valid()
    table = []
    try:
        with open(sys.argv[1],"r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

def check_valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    file_name = sys.argv[1]

    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    return file_name

if __name__ == "__main__":
    main()