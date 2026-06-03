# random_choice()
import random
choices = ['rock','paper','scissor']
score = {'player': 0, 'computer': 0}

print("Welcome to Rock, Paper, Scissors!")
print("You can play as many rounds as you want. Type 'exit' to exit or 'quit' to stop the game.\n")

# random_choice = random.choice(['rock','peper','scissor'])
# user_input = input("Enter your choice (rock, paper, scissor): ").lower()
while True:
    player = input("Choose rock, paper, or scissors: ").lower()
    if player == 'exit' or player == 'quit':
        print("Thanks for playing!")
        break
    
    if player not in choices:
        print("Invalid choice. Please enter rock, paper, or scissor.")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie!")
    elif ((player == 'rock' and computer == 'scissor') or ( player == 'paper' and computer == 'rock') or (player == 'scissor' and computer == 'paper')):
        print("You win!")
        score["player"] += 1
    else:
        print("You Lose! Computer Wins!")
        print("Better Luck Next Time!")
        score["computer"] += 1
    print("Score - You:", score["player"], "| Computer:", score["computer"], "\n")
#   if user_input not in ['rock','paper','scissor']:
#     print("Invalid choice. Please enter rock, paper, or scissor.")
#   else:
#     print(f"Computer chose: {random_choice}")
    