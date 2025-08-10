import random
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif(
        (user_choice =="rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice =="rock")or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "you win"
    else:
        return "computer win"
def play_game():
   user_score = 0
   computer_score = 0
   while True:
       user = get_user_choice()
       computer = get_computer_choice()
       print(f"Computer chose: {computer}")
       result = determine_winner(user, computer)
       print(result)
       if result=="you win":
           user_score += 1
       elif result=="computer win":
           computer_score += 1

       print(f"Your score: {user_score}")
       print(f"Computer score: {computer_score}")
       play_again = input("Do you want to play again? (yes/no): ")
       if play_again != "yes":
           break

play_game()