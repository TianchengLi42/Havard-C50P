from pyfiglet import Figlet
figlet = Figlet()
import sys
import random as ramdon

#print("hello, my name is", sys.argv[1])

#user_input = input("Input:")

#print("Output:")

#print()

def main():
    list_of_fonts = figlet.getFonts()
    try:
        if sys.argv[1] != "-f" and sys.argv[1] == "--font":
            print("Hey you made a typo here")
            sys.exit()
        elif sys.argv[-1] not in list_of_fonts:
            print("That's not a valid font")
            sys.exit()
        #font_choice = sys.argv[-1]
    except IndexError:
        chosen_font = ramdon.choice(list_of_fonts)
        figlet.setFont(font=chosen_font)
        print(figlet.renderText(input("Try it out!")))
    else:
        chosen_font = sys.argv[-1]
        figlet.setFont(font=chosen_font)
        print(figlet.renderText(input("Try it out!")))

main()
print(sys.argv[-1])





# need to check if -f or -font exists
# need to check if the second input is a valid font
# except index error
# then run the randomizer
# if there's no index error, then check for -f or -font and the name of the font

