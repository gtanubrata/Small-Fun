import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

guess = int(input("Guess a number between 1 and 10: "))

play = True

while play:
    if guess < random_number:
        print("Too low, try again!")
        guess = int(input())
    else:
        print("Too high, try again!")
        guess = int(input())
    print("You guessed it! You won!")
    
    play = input("Do you want to keep playing? (y/n) " )
    
    if play == "y":
        guess = int(input("Guess a number between 1 and 10: "))
    else:
        play = False