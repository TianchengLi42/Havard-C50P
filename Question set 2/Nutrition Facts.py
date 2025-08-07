fruit_dictionary = [
    {"fruits": "Apple", "Calories": 130},
    {"fruits": "Avocado", "Calories": 50},
    {"fruits": "Banana", "Calories": 110},
    {"fruits": "Cantaloupe", "Calories": 50},
    {"fruits": "Grapefruit", "Calories": 60},
    {"fruits": "Grapes", "Calories": 90},
    {"fruits": "Honeydew Melon", "Calories": 50},
    {"fruits": "Kiwifruit", "Calories": 90},
    {"fruits": "Lemon", "Calories": 15},
    {"fruits": "Lime", "Calories": 20},
    {"fruits": "Nectarine", "Calories": 60},
    {"fruits": "Orange", "Calories": 80},
    {"fruits": "Peach", "Calories": 60},
    {"fruits": "Pear", "Calories": 100},
    {"fruits": "Pineapple", "Calories": 50},
    {"fruits": "Plums", "Calories": 70},
    {"fruits": "Strawberries", "Calories": 50},
    {"fruits": "Sweet Cherries", "Calories": 100},
    {"fruits": "Tangerine", "Calories": 50},
    {"fruits": "Watermelon", "Calories": 80}
]

def main():
    user_fruit = input("Enter fruit: ").casefold()
    for fruit in fruit_dictionary:
        if user_fruit == fruit["fruits"].casefold():
            print (fruit["Calories"])
            break
        else:
            None

main()