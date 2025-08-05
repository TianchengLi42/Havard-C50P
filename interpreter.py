import operator as op
def interpreter(input):
    x = int(input.split(" ")[0])
    y = str(input.split(" ")[1])
    z = int(input.split(" ")[2])
    if y == "+":
        return float(x+z)
    elif y == "-":
        return float(x-z)
    elif y == "*":
        return float(x*z)
    elif y == "/":
        return round(float(x/z),1)
    else:
        print("Invalid input")

print(interpreter(input("let's do some math")))
