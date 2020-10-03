# This is the classic rock paper scissors game, where a user plays against the computer
# we get user input, whereas the computer plays randomly

from random import randrange, seed
from datetime import datetime

seed(datetime.now())

round = 0
score = [0, 0]  # player,computer scores merged
historylog = []
while True:
    round += 1
    print("Round: " + str(round))

    # use input
    player_choice = input("Choose your move: ")
    while player_choice not in ["rock", "paper", "scissors"]:
        print("You have given the wrong input.Please try again.")
        player_choice = input("Choose your move: ")

    print(player_choice)

    # random computer choice
    computer_choice = randrange(3)
    if computer_choice == 0:
        computer_choice = "rock"
    elif computer_choice == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    # winner check
    if player_choice == "rock":
        if computer_choice == "rock":
            winner = "nobody"
        elif computer_choice == "paper":
            winner = "Computer"
        else:
            winner = "Player"
    elif player_choice == "paper":
        if computer_choice == "rock":
            winner = "Player"
        elif computer_choice == "paper":
            winner = "nobody"
        else:
            winner = "Computer"
    else:
        if computer_choice == "rock":
            winner = "Computer"
        elif computer_choice == "paper":
            winner = "Player"
        else:
            winner = "nobody"

    if winner == "Player":
        score[0] += 1
    elif winner == "Computer":
        score[1] += 1

    # let's log the results
    historylog.append(
        "Round " + str(round) + " :Player:" + player_choice + ", Computer: " + computer_choice + ",Score: " + str(
            score[0]) + "-" + str(score[1]))
    # winning results
    print("Computer picks: " + computer_choice)
    print("The winner is: " + winner)
    print("Player vs Computer:" + str(score[0]) + "-" + str(score[1]))

    if score[0] == 3:
        print("Player has won!")
        print("")
        for history_item in historylog:
            print(history_item)
        break
    elif score[1] == 3:
        print("Computer has won!")
        print("")
        for history_item in historylog:
            print(history_item)
        break

    print("---------------------------------------------- \n")
