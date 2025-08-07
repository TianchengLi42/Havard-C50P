def remaining_cost(money):
    if money < 50:
        return (
            print("You're owned", 50 - money, "dollars, please put in more coins!"))
    else:
        return (None)


def main():
    print("This is a coke vending machine, please put in some coins!")
    money = int(input())
    while money != 50:
        if money > 50:
            print("You put too much coins! Here's your change", money - 50)
            break
        remaining_cost(money)
        money = int(input()) + money
    print("Here's your coke!")

main()