#number guessing game
import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print(f'Pssst, the number is {number}')
print('Easy difficulty has 10 attempts, and Hard Difficulty has 5 attempts.')

def compare(user_guess,actual_answer):
    if user_guess > actual_answer:
        return "Too high."
    elif user_guess < actual_answer:
        return "Too low."
    else:
        return "You got it!"

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5

attempts = difficulty()
while attempts > 0:
    guess = int(input("Make a guess: "))
    print(f'{compare(guess,number)}')
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print(f"You've run out of attempts. The number was {number}")

