import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ")
        if choice.lower() in ['rock', 'paper', 'scissors']:
            return choice.lower()
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'user'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        print("Let's play Stone Paper Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            user_wins += 1
            print("You win!")
        elif winner == 'computer':
            computer_wins += 1
            print("Computer wins!")
        else:
            draws += 1
            print("It's a draw!")

        print(f"Score - User: {user_wins}, Computer: {computer_wins}, Draws: {draws}\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print("Thanks for playing!")

play_game()
