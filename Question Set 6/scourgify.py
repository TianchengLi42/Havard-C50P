import sys
import csv



def checker():
    """checker command checks for if the user has inputted too many arguments"""
    try:
        before = sys.argv[1]
        after = sys.argv[2]
        if sys.argv[-1] != sys.argv[2]:
            print("Too many arguments")
            sys.exit()
        return before, after
    except IndexError:
        print("Too few arguments")
    except FileNotFoundError:
        print("Could not open", before)

def converter(before, after):
    """convert command takes in the inputted strings from the user, reads the appropriate files, makes the appropriate values from the name and house keys, create a list out of the name key to create a first name list and a last name list, and finally, create a new csv file and writes the cleaned data in the new file"""
    students = []
    last_name = []
    first_name = []
    house = []
    with open(before) as file:
        file = csv.DictReader(file, delimiter=",")
        for row in file:
            students.append({"name": row["name"], "house": row["house"]})

        for rows in students:
            last_name.append(rows["name"].split(", ")[0])
            first_name.append(rows["name"].split(", ")[1])
            house.append(rows["house"])


    title = after
    with open(title, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "house"])
        writer.writeheader()
        for row in range(len(first_name)):
            writer.writerow({"first_name": first_name[row], "last_name": last_name[row], "house": house[row]})







def main():
    before, after = checker()
    converter(before, after)


main()