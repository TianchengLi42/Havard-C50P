import re

user_input = input("What is your email address?")
match = re.search(r".+[^@]@[^@].+[^\.]\.[^\.].+", user_input)
if match:
    print("Valid Email Address")
else:
    print("Invalid Email Address")