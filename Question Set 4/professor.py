import random as random


def main():
    user_input = get_level()
    x,y = generate_integer(user_input)
    counter = 0
    score = 0
    while counter != len(x):

        print(x[counter], "+", y[counter])
        answer = x[counter] + y[counter]
        user_guess = int(input())
        if user_guess != answer:
            print("EEE")
        else:
            score = score + 1
            print("Your current score is", score)
        counter += 1
    print("Your final score is ", score)



def get_level():
    while True:
        try:
            level = int(input("enter a number between 1 to 3"))
            if level < 1 or level > 3:
                raise ValueError

        except ValueError:
            print("You've either entered the wrong level, or you've entered something that's not an int, try again.")
        else:
            print("level", level)
            return level





def generate_integer(level):
    x = []
    y = []
    start = 0
    end = 10
    start = pow(0,level)
    end = pow(10,level) - 1
    if start == 0:
        start = 1
    # generating 10 x and y
    counter = 10
    while counter != 0:
        x.append(random.randint(start,end))
        y.append(random.randint(start,end))
        counter = counter - 1
    return(x,y)




if __name__ == "__main__":
    main()
