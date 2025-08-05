# converting :) to 🙂 and :( to 🙁
def convert(text):
    face = text.replace(":)", "🙂").replace(":(","🙁")
    return face

print(convert(convert(input("Enter your message: "))))