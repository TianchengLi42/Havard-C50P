months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# need a def that prints out the yyyy-mm-dd format
# note that yyyy-mm-dd needs to be padded with leading zero for months and dates
# need to check that dd is < 31

def print_date(year, month, day):
    counter = 1
    # for def print, we're going to assume that we've done the work to clean up the input string already
    # and we've got three input variables (year months date)
    # year month and date can be strings
    # first, let's convert these strings into ints
    # if it returns an error, we know that is because of the month, so we use the provided index to change the month to crrensponding int month
    # finally, when printing the final date, we need to make sure that dates and months have leading 0s if they're below 10
    while True:
        try:
            year = int(year)
            day = int(day)
            month = int(month)
            while day > 31:
                print("that's not a valid date, please enter a new date")
                day = int(input())
            while month > 12:
                print("that's not a valid month, please enter a new date")
                month = int(input())

        # This sortes out which month it is
        except ValueError:
            for i in months:
                if i == month:
                    month = counter
                    break
                else:
                    counter = counter + 1
        # This prints out the current, final date format
        else:
            # use fstrings to format the int into giving leading 0
            print(f"{year}-{month:02d}-{day:02d}", sep="")
            break


def cleaner(user_input):
    for char in user_input:
        if char == "/":
            user_input = user_input.split("/")
            year = user_input[-1]
            month = user_input[0]
            day = user_input[1]
            return year, month, day
        else:
            pass
    user_input = user_input.split(" ")
    print(user_input)
    year = user_input[-1]
    month = user_input[0]
    day = user_input[1]
    day = day[:-1]
    return year, month, day


   # for user input, we want to clean up the input of the user into "year, month, and day in string format so that print_date function can understand it"
    # input is 9/8/1636 to 1636/9/8
    # input is September 8, 1636 and it's 1636/9/8

def main():
    year, month, day = cleaner(input("enter your date!"))
    print_date(year, month, day)

main()


#print(print_date("2020", "September", "90"))


