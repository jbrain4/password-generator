import random

class PasswordGenerator:
    def __init__(self):
        # Open the dictionary
        self.dictionary = open("dict.txt")

        # define the symbols to use as separators
        self.symbols = ",.\\/?*&%#@!:;~-_=+"

        self.numberOfWords = 0
        self.minimumWordLength = 0
        self.maximumWordLength = 0
        self.paddingDigitsBefore = 0
        self.paddingDigitsAfter = 0

        # Save the dictionary as an array
        self.words = self.dictionary.readlines()
        self.words[:] = [self.word.rstrip('\n') for self.word in self.words]
        ## DEBUG: print(words)


# GETTERS AND SETTERS BELOW ####################################################
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

    # Set the number of padding digits at the start of the password
    def setPaddingDigitsBefore(self, number):
        self.paddingDigitsBefore = number

    # Get the number of padding digits at the start of the password
    def getPaddingDigitsBefore(self):
        return self.paddingDigitsBefore

    # Set the number of padding digits at the end of the password
    def setPaddingDigitsAfter(self, number):
        self.paddingDigitsAfter = number

    # Get the number of padding digits at the end of the password
    def getPaddingDigitsAfter(self):
        return self.paddingDigitsAfter

    # Set the symbols to use for separators
    def setSeparatorSymbols(self, symbols):
        self.symbols = symbols

    # Get the symbols to use for sepatators
    def getSeparatorSymbols(self):
        return self.symbols


# PASSWORD GENERATOR ###########################################################
    def generatePassword(self):
        password = ""
        currentWord = 0
        startDigitPaddingIndex = 0
        endDigitPaddingIndex = 0
        caseStart = random.randint(0, 9)
        separator = random.choice(self.symbols)

        while startDigitPaddingIndex < self.paddingDigitsBefore:
            password += str(random.randint(0, 9))
            startDigitPaddingIndex += 1

        if self.paddingDigitsBefore > 0:
            password += separator

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

        if self.paddingDigitsAfter > 0:
            password += separator

        while endDigitPaddingIndex < self.paddingDigitsAfter:
            password += str(random.randint(0, 9))
            endDigitPaddingIndex += 1

        return password

    # Close the dictionary file
    def cleanup(self):
        self.dictionary.close()

## DEBUG:
passwd = PasswordGenerator()
passwd.setNumberOfWords(3)
passwd.setMinimumWordLength(4)
passwd.setMaximumWordLength(10)
passwd.setPaddingDigitsBefore(2)
passwd.setPaddingDigitsAfter(2)
passwd.setSeparatorSymbols(",.:-_")
print(passwd.generatePassword())
passwd.cleanup()
