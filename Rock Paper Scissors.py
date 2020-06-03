import random
#Setting the choices
Choices = ["rock", "paper", "scissors"]
#Start of the Loop
while True:
    #Gathering the guesses
    botChoice = Choices[random.randint(0,2)]
    playerChoice = input("Rock, Paper, or Scissors: ").lower()
    #Repeating loop if the player does not guess one of the choices
    while playerChoice not in Choices:
        print("That is not a choice")
        playerChoice = input("Rock, Paper, or Scissors: ").lower()
#Rock + outcomes
    if playerChoice == "rock":
        if botChoice == "rock":
            print("Tie!")
        if botChoice == "paper":
            print("You Lost")
        if botChoice == "scissors":
            print("You Win!")
#Paper + outcomes
    if playerChoice == "paper":
        if botChoice == "rock":
            print("You Win!")
        if botChoice == "paper":
            print("Tie!")
        if botChoice == "scissors":
            print("You Lose!")
#Scissors + outcomes
    if playerChoice == "scissors":
        if botChoice == "rock":
            print("You Lose!")
        if botChoice == "paper":
            print("You Win!")
        if botChoice == "scissors":
            print("Tie!")
