def twttr(letters):
    for letter in letters:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
            print("", end="")
        else:
            print(letter, end='')

def main():
    twttr(input("Enter letters: "))

main()