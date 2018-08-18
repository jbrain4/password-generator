import random

class PasswordGenerator:
    def __init__(self):
        # Open the dictionary
        self.dictionary = open("dict.txt")

        self.numbers = "0123456789"

        # define the symbols to use as separators
        self.symbols = ",.\\/?*&%#@!:;~-_=+"

        self.numberOfWords = 0
        self.minimumWordLength = 0
        self.maximumWordLength = 0

        # Save the dictionary as an array
        self.words = self.dictionary.readlines()
        self.words[:] = [self.word.rstrip('\n') for self.word in self.words]
        ## DEBUG: print(words)


    # GETTERS AND SETTERS BELOW ################################################
    # Set the number of words to use in the password
    def setNumberOfWords(self, number):
        self.numberOfWords = number

    # Get the number of words to use in the password
    def getNumberOfWords(self):
        return self.numberOfWords

    # Set the minimum word length
    def setMinimumWordLength(self, number):
        self.minimumWordLength = number

    # Get the minimum word length
    def getMinimumWordLength(self):
        return self.minimumWordLength

    # Set the maximum word length
    def setMaximumWordLength(self, number):
        self.maximumWordLength = number

    # Get the maximum word length
    def getMaximumWordLength(self):
        return self.maximumWordLength



    def generatePassword(self):
        password = ""
        currentWord = 0
        caseStart = int(random.choice(self.numbers))
        separator = random.choice(self.symbols)
        while currentWord < self.numberOfWords:
            newWord = random.choice(self.words)
            if len(newWord) < self.minimumWordLength or len(newWord) > self.maximumWordLength:
                continue
            else:
                if (caseStart % 2) == 0:
                    password += newWord.upper()
                    caseStart += 1
                else:
                    password += newWord
                    caseStart += 1
            if (currentWord + 1) < self.numberOfWords:
                password += separator
            currentWord += 1
        password += random.choice(self.numbers)
        password += random.choice(self.numbers)
        return password

    # Close the dictionary file
    def cleanup(self):
        self.dictionary.close()

## DEBUG:
passwd = PasswordGenerator()
passwd.setNumberOfWords(3)
passwd.setMinimumWordLength(4)
passwd.setMaximumWordLength(10)
print(passwd.getNumberOfWords())
print(passwd.getMaximumWordLength())
print(passwd.getMinimumWordLength())
print(passwd.generatePassword())
passwd.cleanup()
