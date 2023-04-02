import string
import random

upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

generatedPassword = ''
addSymbols = False

while True:
    try:
        passwordLength = input("Enter the length of your password: ")
        passwordLength = int(passwordLength)
        if passwordLength < 8:
            raise ValueError
        break
    except ValueError:
        print("Enter a valid number greater or equal to 8: ")
        continue

while True:
    try:
        enableSymbols = input("Add symbols to your password? (Type Y/N): ")
        if enableSymbols == 'Y':
            addSymbols = True
        elif enableSymbols == 'N':
            addSymbols == False
        else:
            raise ValueError
        break
    except ValueError:
        print("Enter Y or N: ")
        continue

randomCharacters = upperCase + lowerCase + numbers
if addSymbols == True:
    randomCharacters = upperCase + lowerCase + numbers + symbols


for x in range(passwordLength):
    randomIndex = random.randrange(0,(randomCharacters.__len__()))
    generatedPassword += (randomCharacters[randomIndex])

print(generatedPassword)