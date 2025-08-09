def main():
    plate = input("Plate: ")
    if is_valid(plate) and additional_check(plate) and triple_check(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return_value = True
    # checks if the license plate is at most 6 characters long
    if len(s) > 6:
        return False
    # checking for punctuation marks
    else:
        for i in s:
            if i.isalnum() == False:
                return_value = False
                return return_value
    return return_value


def additional_check(s):
    for characters in s:
        if characters.isdigit():
            # check if the first number is larger or equal to 1, which is not a zero
            if int(characters) >= 1:
                return True
            # if it is a zero, it returns false
            else:
                return False
        # making sure that no number is in the middle of the plate
        elif s[-1].isalpha():
            return False


def triple_check(s):
    count = 0
    for characters in s:
        if characters.isalpha():
            count = count + 1
            print(count)
    if count >= 2:
        return True
    else:
        return False


if __name__ == "__main__":
    main()




