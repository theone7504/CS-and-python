import sys
import os

from PIL import Image, ImageOps

def main():

    check_length()
    check_extension()
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as im:
            photo = ImageOps.fit(im, size=(600, 600))
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])

    except FileNotFoundError :
        sys.exit("Input does not exist")






def check_length() :
    if len(sys.argv)<3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3 :
        sys.exit("Too many command-line arguments")
def check_extension() :
    try :

        name1,extension1 = (sys.argv[1]).split(".")
        name2,extension2 = (sys.argv[2]).split(".")
        if (extension1.lower() != extension2.lower()) :
            sys.exit("Input and output have different extensions")
        if extension1.lower() not in ['jpg','jpeg' ,'png'] or extension2.lower in ['jpg','jpeg' ,'png'] :
            sys.exit("Invalid input")
    except ValueError :
        sys.exit("Invalid input")


if __name__ == "__main__" :
    main()