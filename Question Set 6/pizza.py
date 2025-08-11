import sys
import csv
from tabulate import tabulate

def checker():
    try:
        file = sys.argv[1]
        if file.endswith(".csv") == False:
            print("Not a .csv file")
            sys.exit()
        with open(file) as file:
            reader = csv.reader(file)
            print(tabulate(reader, tablefmt="grid"))

    except IndexError:
        print("Too few arguments")
    except FileNotFoundError:
        print("File not found")

checker()