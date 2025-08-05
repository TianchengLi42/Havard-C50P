def check(value):
    if value.split()[0].casefold() == "Hello":
        return "0$"
    elif value.casefold() == "hello":
        return "0$"
    elif value.casefold().startswith("h"):
        return "20$"
    else:
        return "100$"


print(check(input("Hello, welcome to the bank")))
