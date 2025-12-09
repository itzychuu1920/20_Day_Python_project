import random
symbols = ("rock", "paper", "scissors")
is_running = True
score_player = 0
score_computer = 0
while is_running:
    computer = random.choice(symbols)
    player = input("Enter Your Choice(rock, paper, scissors): ").lower()
    if player not in symbols:
        print("Invalid choice.")
    else:
        if player == computer:
            print("Tie")
            print(f"{score_player}:{score_computer}")
        elif player == "rock" and computer == "scissors":
            print("You Win!")
            score_player += 1
            print(f"{score_player}:{score_computer}")
        elif player == "paper" and computer == "rock":
            print("You Win!")
            score_player += 1
            print(f"{score_player}:{score_computer}")
        elif player == "scissors" and computer == "paper":
            print("You win!")
            score_player += 1
            print(f"{score_player}:{score_computer}")
        else:
            print("You lose")
            score_computer += 1
            print(f"{score_player}:{score_computer}")
    if score_player == 3:
        print(f"You won the match! {score_player}:{score_computer}")
        if input("Do you wanna play again?(Y/n): ").lower() == "y":
            is_running = True
            score_player = 0
            score_computer = 0
        else:
            is_running = False
    elif score_computer == 3:
        print(f"You lost the match! {score_player}:{score_computer}")
        if input("Want a rematch?(Y/n): ").lower() == "y":
            is_running = True
            score_player = 0
            score_computer = 0
        else:
            is_running = False

         

