import random

class PasswordGenerator:
    def __init__(self):
        self.dictionary = open("dict.txt") # Open the word dictionary

        # DEFAULT OPTIONS:
        self.separatorSymbols = ",.\\/?*&%#@!:;~-_=+" # Define the default symbols to use as separators
        self.paddingSymbols = ",.\\/?*&%#@!:;~-_=+" # Define the default symbols to use as padding

        self.numberOfWords = 3 # Define the default number of words to use
        self.minimumWordLength = 4 # Define the default minimum word length
        self.maximumWordLength = 10 # Define the default maximum word length
        self.paddingDigitsBefore = 0 # Define the default number of padding digits to insert before the main part of the password
        self.paddingDigitsAfter = 2 # Define the default number of padding digits to insert after the main part of the password
        self.paddingSymbolsBefore = 0 # Define the default number of padding symbols to insert before the main part of the password
        self.paddingSymbolsAfter = 0 # Define the default number of padding symbols to insert after the main part of the password
        self.paddingToLength = 0 # Define the default length to pad the password to

        # Save the word dictionary as an array
        self.words = self.dictionary.readlines()
        self.words[:] = [self.word.rstrip('\n') for self.word in self.words]


# GETTERS AND SETTERS BELOW ####################################################
    # Set the number of words to use in the password
    def setNumberOfWords(self, amount):
        self.numberOfWords = amount

    # Get the number of words to use in the password
    def getNumberOfWords(self):
        return self.numberOfWords

    # Set the minimum word length
    def setMinimumWordLength(self, amount):
        self.minimumWordLength = amount

    # Get the minimum word length
    def getMinimumWordLength(self):
        return self.minimumWordLength

    # Set the maximum word length
    def setMaximumWordLength(self, amount):
        self.maximumWordLength = amount

    # Get the maximum word length
    def getMaximumWordLength(self):
        return self.maximumWordLength

    # Set the number of padding digits at the start of the password
    def setPaddingDigitsBefore(self, amount):
        self.paddingDigitsBefore = amount

    # Get the number of padding digits at the start of the password
    def getPaddingDigitsBefore(self):
        return self.paddingDigitsBefore

    # Set the number of padding digits at the end of the password
    def setPaddingDigitsAfter(self, amount):
        self.paddingDigitsAfter = amount

    # Get the number of padding digits at the end of the password
    def getPaddingDigitsAfter(self):
        return self.paddingDigitsAfter

    # Set the symbols to use as separators
    def setSeparatorSymbols(self, symbols):
        self.separatorSymbols = symbols

    # Get the symbols to use as sepatators
    def getSeparatorSymbols(self):
        return self.separatorSymbols

    # Set the number of padding symbols at the start of the password
    def setPaddingSymbolsBefore(self, amount):
        self.paddingSymbolsBefore = amount

    # Get the number of padding symbols at the start of the password
    def getPaddingSymbolsBefore(self, amount):
        return self.paddingSymbolsBefore

    # Set the number of padding symbols at the end of the password
    def setPaddingSymbolsAfter(self, amount):
        self.paddingSymbolsAfter = amount

    # Get the number of padding symbols at the end of the password
    def getPaddingSymbolsAfter(self, amount):
        return self.paddingSymbolsAfter

    # Set the number of characters that you want to pad to
    def setPaddingToLength(self, length):
        self.paddingToLength = length

    # Get the number of characters that you want to pad to
    def getPaddingToLength(self):
        return self.paddingToLength


# PASSWORD GENERATOR ###########################################################
    def generatePassword(self, totalPasswords = 1):
        generatedPasswords = [] # Initiate the array that will hold the passwords
        createdPasswords = 0 # Initiate the counter for the created passwords

        # Create the given number of passwords
        while createdPasswords < totalPasswords:
            password = "" # Initiate a blank string to store the created password temporarily
            currentWord = 0 # Initiate a counter for the number of words
            startDigitPaddingIndex = 0  # Initiate a counter for the number of start padding digits
            endDigitPaddingIndex = 0 # Initiate a counter for the number of end padding digits
            startSymbolPaddingIndex = 0 # Initiate a counter for the start padding symbols
            endSymbolPaddingIndex = 0 # Initiate a counter for the end padding symbols
            caseStart = random.randint(0, 9) # Random number used in deciding the starting word case
            separatorSymbols = random.choice(self.separatorSymbols) # Pick a random symbol to be used as a word separator
            paddingSymbols = random.choice(self.separatorSymbols) # Pick a random symbol to be used as padding at the begging and end of password

            # Add the starting padding symbols to the password
            while startSymbolPaddingIndex < self.paddingSymbolsBefore:
                password += paddingSymbols
                startSymbolPaddingIndex += 1

            # Add the starting padding numbers to the password
            while startDigitPaddingIndex < self.paddingDigitsBefore:
                password += str(random.randint(0, 9))
                startDigitPaddingIndex += 1

            # If there are padding numbers, add a separator between the last number and the first word
            if self.paddingDigitsBefore > 0:
                password += separatorSymbols

            # Add the words to the password
            while currentWord < self.numberOfWords:
                # Choose a random word from the dictionary
                newWord = random.choice(self.words)

                # Check the length of the chosen word, make sure it is not too long of too short, if it is, get a new word
                if len(newWord) < self.minimumWordLength or len(newWord) > self.maximumWordLength:
                    continue
                else:
                    # Make the word uppercase if caseStart is even, lowercase if it is odd
                    if (caseStart % 2) == 0:
                        password += newWord.upper()
                        caseStart += 1
                    else:
                        password += newWord
                        caseStart += 1
                # Add a separator if there is another word
                if (currentWord + 1) < self.numberOfWords:
                    password += separatorSymbols
                currentWord += 1

            # If there is a padding number after the last word, add a separator
            if self.paddingDigitsAfter > 0:
                password += separatorSymbols

            # Add the padding numbers
            while endDigitPaddingIndex < self.paddingDigitsAfter:
                password += str(random.randint(0, 9))
                endDigitPaddingIndex += 1

            # Add the padding symbols
            while endSymbolPaddingIndex < self.paddingSymbolsAfter:
                password += paddingSymbols
                endSymbolPaddingIndex += 1

            # Add padding symbols to make the password a specific length
            while len(password) < self.paddingToLength:
                password += paddingSymbols

            # Increment the password counter
            createdPasswords += 1

            # Append the created password to the generated password list
            generatedPasswords.append(password)

        return generatedPasswords # Return the generated passwords
        self.dictionary.close() # Close the dictionary file
