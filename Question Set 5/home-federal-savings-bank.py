def main():
    print(value(input("Hello, welcome to the bank")), "$", sep = "")


def value(greeting):
    if greeting.split()[0].casefold() == "Hello":
        return 0
    elif greeting.casefold() == "hello":
        return 0
    elif greeting.casefold().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

