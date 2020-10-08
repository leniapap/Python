from random import seed
from random import randrange
from datetime import datetime

# globals
score = [
    {
        "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1
    },
    {
        "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1
    }
]


# functions
def roll_dice(n):
    # where n represents number of dice
    dice = []

    for i in range(n):
        dice += [randrange(1, 6 + 1)]
    return sorted(dice)


def player_turn():
    dices_rolling = 5
    dices_kept = []
    for roll in range(3):
        dice = roll_dice(dices_rolling)
        print("-" * 15)
        print(f"Roll: {roll + 1}!")

        if roll in range(2):
            while True:
                print(f"This is your dice: {dice} ")
                choice = input("Do you want to keep a dice?(Type the number or type no)")
                if choice == 'no':
                    break
                elif int(choice) not in dice:
                    print("There is no such choice in your dice")
                else:
                    dices_rolling -= 1
                    dice.remove(int(choice))
                    dices_kept += [int(choice)]
        else:
            dices_kept += dice
    print(f"Your dice is: {dices_kept}")
    return dices_kept


def convert_name(string):
    if string == "ones":
        return 1
    if string == "twos":
        return 2
    if string == "threes":
        return 3
    if string == "fours":
        return 4
    if string == "fives":
        return 5
    if string == "sixes":
        return 6


def player_picks(player, dice):
    print("You can save your dice in the following ways: ", end=",  ")
    picks = []
    for key, value in score[player].items():
        if value == -1:
            print(key, end=", ")
            picks += [key]

    while True:
        choice = input("Please type your choice: ")
        if choice not in picks:
            print("Wrong choice! ")
            continue
        else:
            key_value = convert_name(choice)
            score[player][choice] = dice.count(key_value) * key_value
            return


def print_card(player):
    print(f"Player: {player + 1}")
    if score[player]["ones"] == -1:
        print("ones: ")
    else:
        print(f"ones: {score[player]['ones']}")
    if score[player]["twos"] == -1:
        print("twos: ")
    else:
        print(f"twos: {score[player]['twos']}")
    if score[player]["threes"] == -1:
        print("threes: ")
    else:
        print(f"threes: {score[player]['threes']}")
    if score[player]["fours"] == -1:
        print("fours: ")
    else:
        print(f"fours: {score[player]['fours']}")
    if score[player]["fives"] == -1:
        print("fives: ")
    else:
        print(f"fives: {score[player]['fives']}")
    if score[player]["sixes"] == -1:
        print("sixes: ")
    else:
        print(f"sixes: {score[player]['sixes']}")


def calculate_score(player):
    return sum(score[player].values())


# main function

def main():
    seed(datetime.now())

    for rounds in range(1, 6):
        print("-" * 20)
        print(f"Round: {rounds}!!")
        print("-" * 20)
        for player in range(2):
            print(f"Player:{player + 1}")
            print("-" * 20)
            print_card(player)
            dice = player_turn()
            player_picks(player, dice)
    print("\n\n")
    print_card(0)
    score1 = calculate_score(0)
    print(f"First player's score is: {score1}")
    print_card(1)
    score2 = calculate_score(1)
    print(f"Second player's score is: {score2}")

    if score1 > score2:
        print("Player 1 wins!")
    elif score2 > score1:
        print("Player 2 wins!")
    else:
        print("It is a tie!")


main()
