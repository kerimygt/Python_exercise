import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_size = len(letters) - 1
number_size = len(numbers) - 1
symbols_size = len(symbols) - 1

letters_array = []
numbers_array = []
symbols_array = []

for letter in range(0, nr_letters):
    random_letter = random.randint(0, letters_size)
    letters_array.append(letters[random_letter])

for symbol in range(0, nr_symbols):
    random_symbol = random.randint(0, symbols_size)
    symbols_array.append(symbols[random_symbol])

for number in range(0, nr_numbers):
    random_number = random.randint(0, number_size)
    numbers_array.append(numbers[random_number])

password = []
for value in letters_array:
    password.append(value)
for value in numbers_array:
    password.append(value)
for value in symbols_array:
    password.append(value)

new_list = password.copy()
random.shuffle(new_list)

for i in new_list:
    print(i, end="")
