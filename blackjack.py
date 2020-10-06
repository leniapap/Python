from random import seed
from random import randrange
from datetime import datetime

# globals
kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
deck = {(k, n) for k in kind for n in number}


# functions
def hand_value(hand):
    sum = 0
    ace = False
    for card in hand:
        n = card[1]
        if n == "jack" or n == "king" or n == "queen":
            sum += 10
        elif n == "ace":
            ace = True
            sum += 1
        else:
            sum += n

    if ace:
        if sum + 10 < 21:
            sum += 10
    return sum


def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())

    while True:
        print(hand)
        player_choice = input("H -hit or S -stand")
        if player_choice == "H":
            hand.add(deck.pop())
            if hand_value(hand) >= 21:
                return hand_value(hand)
        elif player_choice == "S":
            return hand_value(hand)


def computer(player_value, hand):
    hand.add(deck.pop())
    hand.add(deck.pop())
    value = hand_value(hand)
    if value >= 21:
        return value
    elif value >= player_value:
        return value
    else:
        hand.add(deck.pop())


# main
def main():
    seed(datetime.now())
    rounds = 0
    score = [0,0] #player, computer
    while True:
        print("=" *15)
        rounds +=1
        print(f"Round: {rounds}")
        print("=" * 15)

        players_hand = set()
        player_value = player(players_hand)

        print(f"{players_hand} with value: {player_value}")
        if player_value == 21:
            print("Congracts!You won!")
            result = "player"
        elif player_value > 21:
            print("You lost :(")
            result = "computer"
        else:
            print("Computer's turn")
            computer_hand = set()
            computer_value = computer(player_value, computer_hand)
            print(f"{computer_hand} with value: {computer_value}")
            if player_value > 21:
                print("Congrats!You won!")
                result = "player"
            else:
                print("You lost!")
                result = "computer"

        if result == "player":
            score[0] += 1
        else:
            score[1] +=1

        print(f"Player score: {score[0]} , Computer score: {score[1]}")
        choice = input("Would you like to play again? Yes or No?")
        if choice == "No":
            break




# start
main()
