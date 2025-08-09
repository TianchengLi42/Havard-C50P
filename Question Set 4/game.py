from random import randint
import random

def main():
    while True:
        try:
            user_input = int(input())
            while user_input < 1:
                print("Pick a number that's larger or equal to 1 please!")
                user_input = int(input())
        except ValueError:
            print("That's not a number!")
        else:
            answer = random.randint(1,user_input)

            while True:
                user_guess = int(input("guess the number!"))
                if user_guess > answer:
                    print("Your guess is too high!")
                elif user_guess < answer:
                    print("Your guess is too low!")
                else:
                    print("That's the right answer!")
                    break
            break
main()
