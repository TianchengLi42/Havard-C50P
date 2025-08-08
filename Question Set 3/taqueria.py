menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# asking the user what thing they want, they would input it, and then input it again, etc
# make sure they haven't inputted an int using a keyerror
# basically, a loop that only breaks when an EOFError
def main():
    cost = 0
    while True:
        try:
            user_input = input("Please enter your order!").title()
            if user_input in menu:
                cost = menu[user_input] + cost
                print("$", end="")
                print(cost)
            else:
                pass
        except EOFError:
            pass
        except KeyError:
            break

main()