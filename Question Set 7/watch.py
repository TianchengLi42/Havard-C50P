import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches = re.search(r".(https?://www\.youtube\.com/)(embed/)?(\w+)(\")?.?", s)
        url = matches.group(1)
        id = matches.group(3)
        shortened_url = re.sub(r"youtube\.com/(embed/)?", "youtu.be/", url)
        parsed_url = shortened_url + id
        return(parsed_url)
    except:
        ValueError
        return(None)

    # one can sub youtube.com into youtu.be, and keep the rest of the string format
    # it may be easier to write ^ conversion first before finding the youtube URL in the HTML string




if __name__ == "__main__":
    main()
