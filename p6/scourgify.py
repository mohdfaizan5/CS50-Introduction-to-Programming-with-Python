#PROGRAM THAT REFORMATES THE output OF GIVEN CSV FILE:
import os, sys, csv, pdb

def main():
    check_valid()
    output = []
    try:
        with open(sys.argv[1],"r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({"first":split_name[1].lstrip(),"last": split_name[0],"house":row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2],"w") as file:
        writer = csv.DictWriter(file,fieldnames=["first","last","house"])
        writer.writerow({"first":"first","last":"last","house":"house"})
        for row in output:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})


def check_valid():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit(f"Could not read {file_name}")
    #for checking if file exists
    with open(file_name) as file:
        file_name = file_name
    # return file_name

if __name__ == "__main__":
    main()