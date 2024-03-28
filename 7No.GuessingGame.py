import random

# python will think of a number between 1 and 6
rNum = random.randint(2, 6)

print("Welcome to guess game! think of a number between 1 and 6")
num = int(input("Think a number : "))
# if user guesses same number as python user win
if num > 6 or num < 1:
    print("Please read the instructions carefully")

elif num == rNum:
    print("YOU WIN! YOU GUESSED IT RIGHT")
else:
    print("You loose")
    print("The number I thought of is " + str(rNum))
