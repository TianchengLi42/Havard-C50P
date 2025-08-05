def playback(text):
    new_text = text.replace(" ", "...")
    return new_text

print(playback(input("Enter your message: ")))