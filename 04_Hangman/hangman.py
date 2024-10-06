import random


def choose_word():
    words = ["python", "code", "javascript", "ibm", "programming", "game", ]
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")

    while attempts < max_attempts:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Wrong guess! {max_attempts - attempts} attempts remaining.")
        else:
            if "_" not in display_word(word_to_guess, guessed_letters):
                print(f"\nCongratulations! You guessed the word: {word_to_guess}")
                break

    if attempts == max_attempts:
        print(f"\nSorry, you ran out of attempts. The word was: {word_to_guess}")


hangman()
