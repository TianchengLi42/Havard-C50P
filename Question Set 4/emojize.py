import emoji as emoji

def emojize(text):
    return emoji.emojize(text, language='en') and emoji.emojize(text, language='alias')

def main():
    print(emojize(input("Emojize your text! ")))

main()
