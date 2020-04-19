import random
difficulty = input("What difficulty would you like? easy, medium or hard\n").lower()

guess_limit = 6
chances_left = 6
guess_taken = 0

while difficulty == "easy":
    try:
        random_number = random.randint(1, 10)
        guess = int(input("Enter a number between 1 - 10: "))
        guess_taken += 1
        chances_left -= 1
        print(f"You have {chances_left} guesses left")
        if random_number == guess:
            print("You got it right")
            break
        elif guess_taken == guess_limit:
            print("Game Over")
            break
        else:
            if guess > random_number:
                print("Your guess was out of range")
            else:
                print("That was wrong")
    except ValueError:
        print("Only numbers are allowed")

guess_limit = 4
chances_left = 4
guess_taken = 0

while difficulty == "medium":
    try:
        random_number = random.randint(1, 20)
        guess = int(input("Enter a number between 1 - 20: "))
        guess_taken += 1
        chances_left -= 1
        print(f"You have {chances_left} guesses left")
        if random_number == guess:
            print("You got it right")
            break
        elif guess_taken == guess_limit:
            print("Game Over")
            break
        else:
            if guess > random_number:
                print("Your guess was out of range")
            else:
                print("That was wrong")
    except ValueError:
        print("Only numbers are allowed")

guess_limit = 3
chances_left = 3
guess_taken = 0

while difficulty == "hard":
    try:
        random_number = random.randint(1, 50)
        guess = int(input("Enter a number between 1 - 50: "))
        guess_taken += 1
        chances_left -= 1
        print(f"You have {chances_left} guesses left")
        if random_number == guess:
            print("You got it right")
            break
        elif guess_taken == guess_limit:
            print("Game Over")
            break
        else:
            if guess > random_number:
                print("Your guess was out of range")
            else:
                print("That was wrong")
    except ValueError:
        print("Only numbers are allowed")