def main():
    user_input = input()
    current_time = convert(user_input)
    if current_time >= 7 and current_time <= 8:
        print("Breakfast time!")
    elif current_time >= 12 and current_time <= 13:
        print("Lunch time!")
    elif current_time >= 18 and current_time <= 19:
        print("Dinner time!")
    else:
        print("It's not meal time yet, please be patient!")


def convert(time):
    hour = float(time.split(":")[0])
    minute = float(time.split(":")[-1]) / 60
    return hour + minute

main()

#if __name__ == "__main__":
#    main()
