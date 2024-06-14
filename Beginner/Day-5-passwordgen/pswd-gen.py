#Password Generator Project
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
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Password order not randomised: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

n = len(password_list)
for i in range(n - 1, 0, -1):
    j = random.randint(0, i)
    password_list[i], password_list[j] = password_list[j], password_list[i]

randomized_password = ""
for char in password_list:
    randomized_password += char

print(f"Password order randomised: {randomized_password}")
