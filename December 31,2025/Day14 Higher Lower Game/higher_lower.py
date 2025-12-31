#Higher Lower Game
import random
from art import logo, vs
from game_data import data

score = 0

while True:
    A = random.choice(data)
    B = random.choice(data)
    
    while A == B:
        B = random.choice(data)

    print(logo[0])
    print(f'Your current score:- {score}')
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(vs[0])
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == 'A' and A['follower_count'] > B['follower_count']:
        print("You got this right!")
        score += 1
    else:
        print("You lost!")
        print(f'Your final score:- {score}')
        break
