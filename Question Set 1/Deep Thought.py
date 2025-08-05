def check(insert):
    if insert == "42":
        return True
    elif insert.casefold() == "forty two":
        return True
    else:
        return False

print(check(input("What is the answer to the great question of life, the universe, and everything ")))