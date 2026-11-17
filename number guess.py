import random
from collections import Counter
import string

# Number Guessing Game
def game():
    num = random.randint(1, 100)
    score = 100
    attempts = 0

    while attempts < 7:
        try:
            guess = int(input("Guess number (1-100): "))
            if not 1 <= guess <= 100:
                print("Enter 1 to 100")
                continue

            attempts += 1

            if guess == num:
                print("Correct! You win!")
                break
            elif guess < num:
                print("Too low!")
            else:
                print("Too high!")

            score -= 10

        except ValueError:
            print("Invalid input!")

    print("Number:", num)
    print("Attempts:", attempts)
    print("Score:", max(score, 0))


# Word Counter
def counter():
    try:
        with open(input("File name: "), "r") as f:
            text = f.read().lower()

        for p in string.punctuation:
            text = text.replace(p, "")

        words = Counter(text.split())

        print("Total words:", sum(words.values()))
        print("Common words:", words.most_common(5))

    except FileNotFoundError:
        print("File not found!")


# Main Menu
while True:
    print("\n1. Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        game()
    elif choice == "2":
        counter()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")