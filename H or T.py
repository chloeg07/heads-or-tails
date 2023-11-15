import random
choices = ["H", "T"]
print("Dont forget capital letters")
userchoice = (input("Choose H or T (heads or tails).........."))
a = random.choice(choices)
if a == userchoice:
    print("you win")
else:
    print("Bad Luck")


