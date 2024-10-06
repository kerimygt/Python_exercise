import random

counter = 0

while True:
    try:
        print("Enter the starting and ending number range in which number you want to guess.")

        start_number = int(input("Enter starting number: "))
        stop_number = int(input("Enter stop number: "))

        random_number = random.randint(start_number, stop_number)

        print("You have the right to guess 3 times")
        for i in range(3):
            user_guess_number = int(input("Please enter the number you guessed :"))
            if random_number == user_guess_number:
                print("Your guess was correct, congratulations")
                break
            elif random_number < user_guess_number:
                print("The number is greater than the number predicted by the computer, guess again")
                counter += 1
            elif random_number > user_guess_number:
                print("The number is less than the number predicted by the computer, guess again")
                counter += 1
            if counter == 3:
                print("Sorry you lost, the computer won")
                break
    except ValueError as e:
        print("Please enter a valid number")
