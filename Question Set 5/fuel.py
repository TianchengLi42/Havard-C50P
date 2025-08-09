

def main():
    user_input = input()
    print(gauge(convert(user_input)))



def convert(fraction):
    X = int(fraction.split("/")[0])
    Y = int(fraction.split("/")[1])
    if Y == 0:
        raise ZeroDivisionError
    elif X > Y:
        raise ValueError
    result = X/Y
    return int(round(result*100, 0))


def gauge(percentage):
    if percentage == 100:
        return("F")
    elif percentage == 0:
        return("E")
    else:
        percentage = (str(percentage))
        percentage = percentage + "%"
        return(percentage)



if __name__ == "__main__":
    main()



# few things we need:
# need to make sure that both x and y are positive (this isn't an exception, but otherwise the answer doesn't make sense)
# need to make sure that Y isn't 0 (0 division error)
# need to make sure that X <= Y (not a strict error, but the answer wont make sense)
# need to make sure that both X and Y are int (Value Error)

