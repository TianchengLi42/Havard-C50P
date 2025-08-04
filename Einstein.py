def convert(mass):
    energy = mass * 300000000 * 300000000
    return energy

print(convert(int(input("Enter your mass: "))))