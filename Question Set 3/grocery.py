# use an infinite loop with break to let users determine when they're done w the grocery list
# sort each unique instances of the input
# print the number of instances each input has occured

def main():
    grocery_list = {}
    counter = 0
    user_input = ""
    while True:
        try:
            user_input = input()
            #print(grocery_list)
            if user_input in grocery_list:
                #print(counter)
                counter = grocery_list[user_input]
                grocery_list[user_input] = counter + 1
                print(grocery_list)
                print(counter)
                counter = 0
            else:
                grocery_list[user_input] = 1


        except EOFError:
            for fruit in sorted(grocery_list):
                print(grocery_list[fruit], end=" ")
                print(fruit.upper())
            break

main()