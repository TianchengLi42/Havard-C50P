import sys

def checker():
    count = 0
    try:
        file = sys.argv[1]
        if file.endswith(".py") == False:
            print("Not a .py file")
            sys.exit()
        with open(file) as file:
            for line in file:
                line = line.lstrip(" ")
                if line[0] == "#" or line[0] == "\n" or line.startswith("#"):
                    continue
                else:
                    count += 1

        print(count)

    except IndexError:
        print("Too few arguments")
    except FileNotFoundError:
        print("File not found")

checker()
#variable = "thing.stuff"
#variable = variable.startswith("thing")
#print(variable)