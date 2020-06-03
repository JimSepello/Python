import random, time
#Setting up the lists to draw characters from
setupList = []
holdVariables = ["U", "L", "N", "S"]
lowerLetters = list("abcdefghijklmnopqrstuvwxyz")
upperLetters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("123456789")
specialCharacters = list("!@#$%^&*")
#User can set how long the password will be
charLimit = int(input("How many characters?: "))
#Holding 'function' calls using letters
for int in range(0, charLimit):
    setupList.append(holdVariables[random.randint(0,3)])
#Printing the characters that make up the password
for item in setupList:
    if item == "U":
        print("{}".format(upperLetters[random.randint(0, 25)]), end="")
    if item == "L":
        print("{}".format(lowerLetters[random.randint(0, 25)]), end="")
    if item == "N":
        print("{}".format(numbers[random.randint(0, 8)]), end="")
    if item == "S":
        print("{}".format(specialCharacters[random.randint(0, 7)]), end="")
print("")
#Pausing for 1 hour
time.sleep(3600)
