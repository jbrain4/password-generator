import random

# Open the dictionary
dictionary = open("dict.txt")

# Save the dictionary as an array
words = dictionary.readlines()
words[:] = [word.rstrip('\n') for word in words]
## DEBUG: print(words)

numbers = "0123456789"
symbols = ",.\\/?*&%#@!:;~-_=+"

numberOfWords = 3
wordLengthMinimum = 4
wordLengthMaximum = 10

password = ""

def generatePassword(wordTotal, min, max):
    password = ""
    currentWord = 0
    caseStart = int(random.choice(numbers))
    separator = random.choice(symbols)
    while currentWord < wordTotal:
        newWord = random.choice(words)
        if len(newWord) < min or len(newWord) > max:
            continue
        else:
            if (caseStart % 2) == 0:
                password += newWord.upper()
                caseStart += 1
            else:
                password += newWord
                caseStart += 1
        if (currentWord + 1) < wordTotal:
            password += separator
        currentWord += 1
    password += random.choice(numbers)
    password += random.choice(numbers)
    return password

print(generatePassword(numberOfWords, wordLengthMinimum, wordLengthMaximum))
dictionary.close()
