# collaborated with Priyanshu Sharma P.4
#title
print("Dice Game Result Checker")
#get input & str -> int
try:
    roll = int(input("Enter dice roll (1-6): "))
#classifier
    if roll < 1 or roll > 6:
        print("Invalid roll. Please enter a number from 1 to 6.")
    elif roll == 6:
        print("You win something BIG!")
    elif roll == 3 or roll == 4 or roll == 5:
        print("You win something small.")
    else:
        print("YOU LOSE!")
#syntax statement
#also the hardest part to debug for all 3 coding mini-projects.
#testing helped find logical problems with the conditionals, and try new ways to solve problems, like the try and except function, which ended up being my best plan.
#i like to use comments, but im definetly going to check my code with a partner to gain feedback from them as well.
except ValueError:
    print("Invalid input. Please enter a number.")