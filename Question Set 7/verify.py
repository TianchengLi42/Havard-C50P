import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # we can separate each ip address input into 4 distinct groups, and check if each groups is over 255 or not
    #if re.search(r"^(\d+\.){3}(\d+)$", ip):
    if re.search(r"^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d+)$", ip):
        return "Valid"
    else:
        return "Invalid"

    ...


...

if __name__ == "__main__":
    main()
