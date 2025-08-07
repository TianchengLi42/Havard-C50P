def convert(user_input):
    for letter in user_input:
        if letter.isupper():
            print("_", end="")
            print(letter.lower(), end="")
        else:
            print(letter, end = "")


convert(input("enter your camel case here, I will convert it to snake case: "))
