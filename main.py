import random

class PasswordGenerator:
    def __init__(self):
        # Open the dictionary
        self.dictionary = open("dict.txt")

        self.numbers = "0123456789"
        self.symbols = ",.\\/?*&%#@!:;~-_=+"

        # Save the dictionary as an array
        self.words = self.dictionary.readlines()
        self.words[:] = [self.word.rstrip('\n') for self.word in self.words]
        ## DEBUG: print(words)

    def generatePassword(self, wordTotal, min, max):
        password = ""
        currentWord = 0
        caseStart = int(random.choice(self.numbers))
        separator = random.choice(self.symbols)
        while currentWord < wordTotal:
            newWord = random.choice(self.words)
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
        password += random.choice(self.numbers)
        password += random.choice(self.numbers)
        return password
    def cleanup(self):
        self.dictionary.close()

passwd = PasswordGenerator()
numberOfWords = 3
wordLengthMinimum = 4
wordLengthMaximum = 10
print(passwd.generatePassword(numberOfWords, wordLengthMinimum, wordLengthMaximum))
passwd.cleanup()
