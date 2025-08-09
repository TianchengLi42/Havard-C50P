def shorten(word):
    output = ""
    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
            output += ""
        else:
            output += letter
    return output

def main():
    print(shorten(input("Enter letters: ")))

if __name__ == "__main__":
    main()

