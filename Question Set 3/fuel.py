def main():
    print("Hello! test how much fuel is left in your fuel tank")
    while True:
        try:
            user_input = input()
            X = int(user_input[0])
            Y = int(user_input[-1])
            result = X/Y
            while True:
                if X > Y:
                    print("You're violating the laws of physics, please input a new number!")
                    user_input = input()
                    X = int(user_input[0])
                    Y = int(user_input[-1])
                elif Y == 0:
                    print("Hey! You entered a zero for the divisor, please try again")
                    user_input = input()
                    X = int(user_input[0])
                    Y = int(user_input[-1])
                else:
                    break
        except ValueError:
            print("Hey! that isn't an integer! Please try again")
        except ZeroDivisionError:
            print("Hey! You entered a zero for the divisor, please try again")
        else:
            if X/Y == 1:
                print("F")
            elif X/Y == 0:
                print("E")
            else:
                print(round(X/Y*100), "%")
            break





main()


# few things we need:
# need to make sure that both x and y are positive (this isn't an exception, but otherwise the answer doesn't make sense)
# need to make sure that Y isn't 0 (0 division error)
# need to make sure that X <= Y (not a strict error, but the answer wont make sense)
# need to make sure that both X and Y are int (Value Error)

