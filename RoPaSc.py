import random

def play_rps():
    choices = ['Rock', 'Paper', 'Scissors']
    
    user_choice = input("Choose Rock, Paper or Scissors: ")
    computer_choice = random.choice(choices)

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        result = "It's a tie!"
        
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
        
    else:
        result = "You lose!"

    print("Result:", result)

play_rps()
