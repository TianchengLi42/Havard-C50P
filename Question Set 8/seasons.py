from datetime import date
import inflect
import datetime
import re

def main():
    print(user_time())

def user_time():
    p = inflect.engine()
    user_input = input("Enter your date of birth in YYYY-MM-DD: !")
    matches = re.search(r"^[1-2]\d{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$", user_input)
    if matches:
        try:
            bdate = datetime.datetime.strptime(user_input, "%Y-%m-%d")
            diff = datetime.date.today() - bdate.date()
            minutes = round(diff.total_seconds() / 60,0)
            minutes = int(minutes)
            minutes = p.number_to_words(minutes)
            return minutes
        except ValueError:
            print("Invalid date")

    else:
       print("Invalid date")


if __name__ == "__main__":
    main()
