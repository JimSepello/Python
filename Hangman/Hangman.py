import random, os, sys, time
#Importing the list of words
with open(os.path.join(sys.path[0], "hmWords.txt"), "r") as f:
    Words = f.read().splitlines()
#Setting variables
newWord = list(Words[random.randint(0, 199)])
CurrentOutput, CorrectGuesses, Remaining = [], [], int(len(newWord)+3)
#Setting up a list to string function for CurrentOutput
def Output():
    str1 = ""
    List = CurrentOutput[:]
    for item in List:
        str1 += item
    print(str1)
#Printing the blank word outside of the loop so it doesn't reset
for item in newWord:
    if item in CorrectGuesses:
        CurrentOutput.append(item)
    else:
        CurrentOutput.append("_")
Output()
#Start of main loop
while True:
    print("Guesses Remaining: {}".format(Remaining))
    #If guesses are = to 0 then you lose and then it resets
    if Remaining == 0:
        print("You Lose")
        time.sleep(3)
        print("")
        newWord = list(Words[random.randint(0, 199)])
        CurrentOutput, CorrectGuesses, Remaining = [], [], int(len(newWord)+3)
        for item in newWord:
            if item in CorrectGuesses:
                CurrentOutput.append(item)
            else:
                CurrentOutput.append("_")
        Output()
    Guess = input("Guess a letter: ").lower()
    #Debug mode
    if Guess == "debug":
        print(newWord)
        Remaining += 1
    # if the Guess is in the word then add it to CorrectGuesses
    if Guess in newWord:
        if Guess not in CorrectGuesses:
            CorrectGuesses.append(Guess)
    #If it isn't in the word then Remaining goes down by 1
    #and prints the CorrectGuesses section of the blank word
    if Guess not in newWord:
        Remaining -= 1
    CurrentOutput = []
    for item in newWord:
        if item in CorrectGuesses:
            CurrentOutput.append(item)
        else:
            CurrentOutput.append("_")
    Output()
    #If you got everything right, congratulate the user then reset
    if CurrentOutput == newWord:
        print("You Win!")
        time.sleep(3)
        print("")
        newWord = list(Words[random.randint(0, 199)])
        CurrentOutput, CorrectGuesses, Remaining = [], [], int(len(newWord)+3)
        for item in newWord:
            if item in CorrectGuesses:
                CurrentOutput.append(item)
            else:
                CurrentOutput.append("_")
        Output()
