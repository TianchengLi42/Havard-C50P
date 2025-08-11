import sys
from PIL import Image

import PIL.Image
import PIL.ImageOps

def checker():
    """checker command checks for if the user has inputted too many/too little arguments"""
    try:
        before = sys.argv[1]
        after = sys.argv[2]
        if sys.argv[-1] != sys.argv[2]:
            print("Too many arguments")
            sys.exit()
        elif before.split(".")[-1] != after.split(".")[-1]:
            print("The file types do not match")
            sys.exit()
        elif before.split(".")[-1] not in ["png", "jpg", "jpeg"]:
            print(before.split(".")[-1] + " is not a valid file type")
            sys.exit()
        return before, after
    except IndexError:
        print("Too few arguments")
    except FileNotFoundError:
        print("The input file doesn't exist!")

def edit(before, after):
    shirt = Image.open(after).convert("RGBA")
    shirt = shirt.resize((900,900))
    muppet = Image.open(before)
    print(shirt.size)
    print(muppet.size)
    muppet.paste(shirt, (190, 500))
    muppet.save("result.jpg")
    muppet.show()


before, after = checker()
edit(before, "after.png")
#shirt = Image.open("after.png").convert("RGBA")
##muppet = Image.open("before1.png").convert("RGBA")
#muppet.paste(shirt, (300, 900))
#muppet.show()

