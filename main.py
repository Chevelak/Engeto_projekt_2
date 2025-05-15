#"""
#projekt_2.py: druhý projekt do Engeto Online Python Akademie

#author: Tomáš Vlach
#mail: vlacht@centrum.cz
#"""

#import
import random

#uvítání
lines = "-" * 35
print("\t\tHi there!")
print(lines)
print("I've generated a random 4 digit number for you")
print("Let's play a bulls and cows game.")
print(lines)
print("Enter a number:")
print(lines)

#tajné číslo
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lenght = 4
first_digit = random.choice(numbers[1:])
remaining_numbers = numbers.copy()
remaining_numbers.remove(first_digit)
remaining_numbers = random.sample(remaining_numbers, lenght - 1)
password = [first_digit] + remaining_numbers
passw = "".join(password)

#počítání bulls a cows  
def evaluate_guess(secret, guess):
    bulls = 0
    cows = 0
    secret_list = list(secret)  
    guess_list = list(guess)    
    used_secret = [False] * 4   
    used_guess = [False] * 4    
   
    #bulls
    for i in range(4):
        if guess_list[i] == secret_list[i]:
            bulls += 1
            used_secret[i] = True
            used_guess[i] = True

    #cows
    for i in range(4):
        if not used_guess[i]:
            for j in range(4):
                if not used_secret[j] and guess_list[i] == secret_list[j]:
                    cows += 1
                    used_secret[j] = True
                    break

    return bulls, cows

#hra a podmínka 
secret_code = passw
attempts = 0
print("Guess the 4-digit secret code (no zeros at the beginning, no duplicates):")

while True:
    number = input("Enter a number:")

    if not number.isdigit():
        print("Must contain only numbers!")
        continue
    elif number[0] == "0":
        print("Must not start with zero!")
        continue
    elif len(number) != len(set(number)):
        print("Must no contain duplicates!")
        continue
    elif len(number) != 4:
        print("The number must have 4 digits!")
        continue
    else:
        print(f">>> {number}")

    guess = number
    attempts += 1
    bulls, cows = evaluate_guess(secret_code, guess)

    if bulls == 4:
        print(f"Coingratulations! You guessed the code {''.join(secret_code)} in {attempts} attempts.")
        break
    else:
        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_word}, {cows} {cow_word}")
