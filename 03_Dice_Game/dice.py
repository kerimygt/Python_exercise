import random


def roll_the_dice():
    return random.randint(1, 6)


def dice_game():
    print("Welcome to the Dice Game!")
    input("Press Enter to get started...")

    while True:
        input("Press Enter to roll the dice...")
        dice1 = roll_the_dice()
        dice2 = roll_the_dice()
        total = dice1 + dice2

        print(f"Dice rolled : {dice1} {dice2}")
        print(f"Total: {total}")

        if total == 7 or total == 11:
            print("congratulations you won")
        elif total == 2 or total == 3 or total == 12:
            print("I'm sorry you lost")
        go_on = input("Do you want to continue? (Yes or No):")
        if go_on.lower() != 'yes':
            break


roll_the_dice()
dice_game()
