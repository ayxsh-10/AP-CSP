#title
print("Dice Game Result Checker")
#get input & str -> int
try:
    roll = int(input("Enter dice roll (1-6): "))
#classifier
    if roll < 1 or roll > 6:
        print("Invalid roll. Please enter a number from 1 to 6.")
    elif roll == 6:
        print("You win big! Jackpot!")
    elif roll == 3 or roll == 4 or roll == 5:
        print("You win something small.")
    else:
        print("Looks like you lost this round. Better luck next time!")
#syntax statement
except ValueError:
    print("Invalid input. Please enter a number.")