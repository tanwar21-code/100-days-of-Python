#making rock , paper , scissor game
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    computer_choice = random.randint(0, 2)
    choices = ["Rock", "Paper", "Scissor"]
    print(f"You chose {choices[user_choice]}")
    print(f"Computer chose {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")