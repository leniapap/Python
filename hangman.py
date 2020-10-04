from random import seed
from datetime import datetime
from random import randrange

seed(datetime.now())
words= [ "kick",
"virgin",
"earthwax",
"charismatic",
"cancer",
"patch",
"discipline",
"shell",
"weed",
"smile",
"electron",
"shift",
"mile",
"stem",
"addition"]

hidden_word = words[randrange(len(words))]
print(hidden_word)
guessed_letters = []
max_rounds=10

for round in range(1 , max_rounds+1):
    print(f"Round:{round}")

    letter = input("Please give a letter: ")

    guessed_letters.append(letter.lower())
    print( f"Letter {letter} exists {hidden_word.count(letter)} times in hidden word.")

    found = True
    for char in hidden_word:
        if char in guessed_letters:
            print(char,end="")
        else:
            print("_",end="")
            found = False
    print(" ")
    if found:
        print("End of game.You won!")
        break
else:
    print("Sorry.Maximum round reached!")
    print(f"The word was: {hidden_word}")