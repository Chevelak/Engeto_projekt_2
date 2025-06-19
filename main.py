#"""
#projekt_2.py: druhý projekt do Engeto Online Python Akademie

#author: Tomáš Vlach
#mail: vlacht@centrum.cz
#"""

#import
import random

#def pro generování tajného kodu
def generate_secret_code(length = 4):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    first_digit = random.choice(numbers[1:])
    remaining_numbers = numbers.copy()
    remaining_numbers.remove(first_digit)
    remaining_numbers = random.sample(remaining_numbers, length - 1)
    password = [first_digit] + remaining_numbers
    return "".join(password)

#def pro správné zadání kodu
def is_valid_guess(guess):
    return (
        guess.isdigit() and
        guess[0] != "0" and
        len(guess) == 4 and
        len(set(guess)) == 4
    )

#def pro bulls a cows
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

#def hlavní tělo
def main():
    secret = generate_secret_code()
    attempts = 0
    lines = "-" * 66

    print("Welcome to The Bulls and Cows game!".center(66))
    print(lines)
    print("The random 4 digit number was generated for you.".center(66))
    print("Let's roll!".center(66))
    print(lines)
    
    print("Guess the 4-digit secret code (no leading zero, no duplicates).".center(66))

    while True:
        print(lines)    
        guess = input("Your guess: ")
                
        if not is_valid_guess(guess):
            print("Invalid input! Must be 4 digits, no leading zero, no duplicates.")
            continue

        print(f">>> {guess}")
               
        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)
       
        if bulls == 4:
            print(f"Congratulations! You guessed the code {secret} in {attempts} attempts")
            break
        else:
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bull_word}, {cows} {cow_word}")

if __name__ == "__main__":
    while True:
        main()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            break
