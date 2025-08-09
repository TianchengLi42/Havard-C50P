user_input = []
import inflect
p = inflect.engine()


#user_input = input("enter your name")
#name_list.append(user_input)
#print("adieu, adieu,", str(name_list))
def main():
    while True:
        try:
            user_input.append(input())
        except EOFError:
            print("adieu, adieu to", end = " ")
            print(p.join(user_input, sep=","))
            break
main()