import random

print("ROCK PAPER SCISSORS")
print("First player to get 3 points wins!")

choices = ["rock", "paper", "scissors"]

player_score = 0
opponent_score = 0

for round_no in range(1, 6):

    print("\nRound", round_no)

    player = input("Choose rock, paper or scissors: ").strip().lower()

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    opponent = random.choice(choices)

    print("Opponent chose:", opponent)

    if player == opponent:
        print("It is a tie!")

    elif (player == "rock" and opponent == "scissors") or \
         (player == "paper" and opponent == "rock") or \
         (player == "scissors" and opponent == "paper"):

        print("You won this round!")
        player_score += 1

    else:
        print("You lost this round!")
        opponent_score += 1

    print("Score:", player_score, "-", opponent_score)

    if player_score == 3 or opponent_score == 3:
        break

print("\n FINAL RESULT ")

if player_score > opponent_score:
    print("You won the match!")

elif opponent_score > player_score:
    print("You lost the match!")

else:
    print("The match is a tie!")

print("Your score:", player_score)
print("Opponent score:", opponent_score)
