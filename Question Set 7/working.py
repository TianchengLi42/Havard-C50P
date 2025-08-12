import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"^((1[0-2])|[1-9]):?([0-5][0-9])? (A|P)M to ((1[0-2])|[1-9]):?([0-5][0-9])? (A|P)M", s)
        first_hour = matches.group(1)
        first_minute = matches.group(3)
        second_minute = matches.group(7)
        AMPM1 = matches.group(4)
        second_hour = matches.group(5)
        AMPM2 = matches.group(8)
    except AttributeError:
        return ValueError
    if first_minute == None:
        first_minute = "00"
    if second_minute == None:
        second_minute = "00"

    if "A" == AMPM1:
        if first_hour == "12":
            hour1 = str(0)+ ":"+ first_minute
        hour1 = first_hour+ ":"+ first_minute

    elif "P" == AMPM1:
        hour1 = str(int(first_hour)+12)+ ":"+ first_minute
    if "A" == AMPM2:
        if second_hour == "12":
            hour1 = str(0)+ ":"+ first_minute
        hour2 = second_hour+ ":"+ second_minute
    elif "P" == AMPM2:
        hour2 = str(int(second_hour)+12)+ ":"+ second_minute

    return(hour1 + " to " + hour2)



if __name__ == "__main__":
    main()
