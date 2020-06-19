import random, os, sys, time
with open(os.path.join(sys.path[0], "hmWords.txt"), "r") as f:
    Words = f.read().splitlines()
#Defining Reset
def Reset():
    global newWord, CurrentOutput, CorrectGuesses, Remaining, ClearWord
    ClearWord= Words[random.randint(0, 199)]
    newWord = list(ClearWord)
    CurrentOutput, CorrectGuesses, Remaining = [], [], int(len(newWord)+3)
#Defining DisplayCurrent
def DisplayCurrent():
    global CurrentOutput, newWord
    CurrentOutput = []
    print("Current Guesses: ", end="")
    for item in newWord:
        if item in CorrectGuesses:
            CurrentOutput.append(item)
        else:
            CurrentOutput.append("_")
    str1, List = "", CurrentOutput[:]
    for item in List:
        str1 += item
    print(str1)
#Defining Prompt
def Prompt():
    time.sleep(3)
    global End
    Continue = input("Play again? (y/n): ").lower()
    if Continue == 'y' or Continue == 'yes':
        End = False
        print(" ")
    else:
        exit()
#Start
Reset()
print("")
print("WELCOME to HANGMAN (To Exit type exit)")
DisplayCurrent()
End = False
while End == False:
    print("Guesses Remaining: {}".format(Remaining))
    if Remaining == 0:
        print("You lose, the word was: {}".format(ClearWord))
        Prompt()
        Reset()
        DisplayCurrent()
        print("Guesses Remaining: {}".format(Remaining))
    Guess = input("Guess a letter: ").lower()
    #For visual clarity
    print(" ")
    #Debug mode
    if Guess == "debug":
        print(newWord)
        Remaining += 1
    #if guess is Exit then exit
    if Guess.lower() == "exit":
        exit()
    #If guess is right and is already guessed, do nothing, else add it to correct
    if Guess in newWord:
        if Guess not in CorrectGuesses:
            CorrectGuesses.append(Guess)
    #If guess is wrong, take off a chance
    if Guess not in newWord:
        Remaining -= 1
    DisplayCurrent()
    #Winning circumstances
    if CurrentOutput == newWord:
        print("Contratulations, You Win!")
        Prompt()
        Reset()
        DisplayCurrent()
