#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Create index for each character class & password list
letters_index = len(letters) - 1
symbols_index = len(symbols) - 1
numbers_index = len(numbers) - 1
password_list = []

# Add letters to password string
for letter in range(0, nr_letters):
  password_list.append(letters[random.randint(0, letters_index)])

# Add symbols to password string
for symbol in range(0, nr_symbols):
  password_list.append(symbols[random.randint(0, symbols_index)])

# Add numbers to password string
for number in range(0, nr_numbers):
  password_list.append(numbers[random.randint(0, numbers_index)])

# Easy answer, password in letter, symbol, number order
password_string = "".join(password_list)
print("Character class order (letter, symbol, number):")
print(password_string)

# Hard answer, randomize the characters
random.shuffle(password_list)
password_string_randomized = "".join(password_list)
print("\nRandomized:")
print(password_string_randomized)
