#PROGRAM THAT TAKES INPUT IMAGE AND PASTES A CS50 SHIRT PNG ON IT
import os, sys, csv
# import PIL as Image
from PIL import Image, ImageOps

def check_valid():

    # print(len(sys.argv))
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file_name = sys.argv[1]
    # print(sys.argv[1])
    file_name = str(file_name)

    # S2: If file’s name does not end in (".png",".jpg",".jpeg") or if the specified file does not exist,
                # the program should instead exit via sys.exit.
    supported_ext = ["jpg","jpeg","png"]
    ext1 = file_name.split(".")[-1]
    ext2 = sys.argv[2].split(".")[-1]

    if ext1 not in supported_ext:
        sys.exit(f"Invalid input")

    #check same extension
    if ext1 != ext2:
        sys.exit(f"Input and output have different extensions")

    return file_name


def main(file_name=check_valid()):
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    #open shirt file
    shirtfile = Image.open("shirt.png")
    #get file size
    size = shirtfile.size

    #resize the input image to fit size
    muppet = ImageOps.fit(imagefile, size)

    #paste shirt on muppet
    muppet.paste(shirtfile,shirtfile)

    #save the photo
    muppet.save(sys.argv[2])
try:
    main()
except FileNotFoundError:
    sys.exit("Input does not exist")
