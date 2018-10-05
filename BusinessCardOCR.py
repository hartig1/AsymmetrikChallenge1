import csv
#use a csv full of names to determine what a name is
global nameDict
with open("names.csv") as names:
    nameDict = {}
    reader = csv.reader(names,delimiter=",")
    for line in reader:
        if(line != []):
            #line[0] is the name(dictionary key)
            #line[1] is the rank(dictionary value) of commonality, with rank 1 being the most common name
            nameDict[line[0].lower()] = int(line[1])
#holds business card data
#constructed with a single argument of a strings from the OCR, that contains the whole business card
class ContactInfo():
    #initialized with a string from the OCR
    def __init__(self, fullBusinessCard):
        self.fullBusinessCard = fullBusinessCard
        self.name = None
        self.phoneNumber = None
        self.email = None
        #automatically sets values
        self.setContactInfo()
    def getName(self):
        if(self.name == ""): #set name in case it's not there (it should always be there)
            self.setName(self.fullBusinessCard.split("\n"))
        return self.name
    def getPhoneNumber(self):
        if(self.phoneNumber == ""): #set number in case it's not there (it should always be there)
            self.setPhoneNumber(self.fullBusinessCard.split("\n"))
        return self.phoneNumber
    def getEmailAddress(self):
        if(self.email == ""): #set email in case it's not there (it should always be there)
            self.setEmail(self.fullBusinessCard.split("\n"))
        return self.email
    #returns the entire business card string, the thing that is input in constructor
    def getOCR(self):
        return self.OCR
    #initialization function, sets all variables
    def setContactInfo(self):
        self.setName()
        self.setPhoneNumber()
        self.setEmailAddress()
    def setName(self):
        lines = self.fullBusinessCard.split("\n")
        nameGuess = ""
        #use the rank of names to determine which one is most likely the name, rank will be stored in bestMatch
        bestMatch = 99999999
        for line in lines:
            if(len(line.split(" ")) < 4): #assume a name will have 3 or less words, can easily be changed or removed if assumption is bad
                for word in line.split(" "):
                    if(word.lower() in nameDict): #check if each word on a line is in the name dictionary
                        if(nameDict[word.lower()] < bestMatch): #check if this name is a better(lower) rank than the best one
                            #this needs to be done because the list of names has some words that are unlikely to be names
                            #but they could appear elsewhere on the card, an example is "engineer" which appears in the name dictionary but isn't likely a name
                            bestMatch = nameDict[word.lower()]
                            nameGuess = line
        if(nameGuess == ""): #we didnt find a name and need the user to tell us what it is
            self.correctName()
            return
        else:
            self.name = nameGuess
    def setPhoneNumber(self):
        lines = self.fullBusinessCard.split("\n")
        potentialNumbers = []
        potentialLines = []
        for line in lines:
            numbers = sum(character.isdigit() for character in line)
            if(numbers == 10 or numbers == 11): #assumption that phone numbers contain 10 or 11 digits, can easily be expanded if needed
                number = ""
                for character in line:
                    if(character.isdigit()): #grab all digits to remove alpha characters
                        number += character
                potentialNumbers.append(number) #add to potential numbers
                potentialLines.append(line.lower())
        if(len(potentialNumbers) == 0): #didn't find anything that resembles a number so the user must tell us what the number is
            self.correctNumber()
        elif(len(potentialNumbers) == 1): #exactly one number so it must be the phone number
            self.phoneNumber = potentialNumbers[0]
        else: #multiple numbers like phone number and fax number from example 2 and 3
            numberSigns = ['phone','cell','tel','number', 'home', 'work', 'telephone'] #a list of words that could be in a line that signifies it is a phone number, can be expanded
            for line in range(0,len(potentialLines)): #loop over lines and number signs to see if theres a match
                for sign in numberSigns:
                    if(sign in potentialLines[line]):
                        self.phoneNumber = potentialNumbers[line]
        if(self.phoneNumber == ""): #if we still haven't found a number the user must tell us which line it is
            self.correctNumber()
    def setEmailAddress(self):
        lines = self.fullBusinessCard.split("\n")
        emailNotifiers = ['@','.edu','.com','.net','.gov'] #signs that a line has an email address
        for line in lines:
            if(emailNotifiers[0] in line): #emails must have an @, but can have any of the other endings
                #if statement makes sure only one of the .com endings is in the string
                if(xor(xor(xor(emailNotifiers[1] in line, emailNotifiers[2] in line), emailNotifiers[3] in line),emailNotifiers[4] in line)):
                    self.email = line #take the first email, could be expanded to make a list of emails if needed
                    break
    #allows user to set the name if the system cannot figure it out
    def correctName(self):
        lines = self.fullBusinessCard.split("\n")
        print("Unable to auto detect name")
        for i in range(0,len(lines)):
            print(str(i+1) + ": " + lines[i])
        lineNum = raw_input("Please input the line number from above that has the name on it: ")
        if(lineNum ==""):
            print("Invalid line, please try again")
            self.correctName()
            return
        try:
            lineNum = int(lineNum)
        except:
            print("Invalid line, please try again")
            self.correctName()
            return
        if(lineNum < 1 or lineNum > len(lines)):
            print("Invalid line, please try again")
            self.correctName()
            return
        lineNum -= 1
        self.name = lines[lineNum]
    #allows user to set the phone number if the system cannot figure it out
    def correctNumber(self):
        lines = self.fullBusinessCard.split("\n")
        print("Unable to auto detect number")
        for i in range(0,len(lines)):
            print(str(i+1) + ": " + lines[i])
        lineNum = input("Please input the line number from above that has the number on it: ")
        try:
            lineNum = int(lineNum)
        except:
            print("Invalid line, please try again")
            self.correctNumber()
            return
        if(lineNum < 1 or lineNum > len(lines)):
            print("Invalid line, please try again")
            self.correctNumber()
            return
        lineNum -= 1
        number = ""
        for character in lines[lineNum]:
            if(character.isdigit()): #grab all digits to remove alpha characters
                number += character
        self.phoneNumber = number
    #allows user to set the email if the system cannot figure it out
    def correctEmail(self):
        lines = self.fullBusinessCard.split("\n")
        print("Unable to auto detect email")
        for i in range(0,len(lines)):
            print(str(i+1) + ": " + lines[i])
        lineNum = input("Please input the line number from above that has the email on it: ")
        try:
            lineNum = int(lineNum)
        except:
            print("Invalid line, please try again")
            self.correctEmail()
            return
        if(lineNum < 1 or lineNum > len(lines)):
            print("Invalid line, please try again")
            self.correctEmail()
            return
        lineNum -= 1
        self.email = lines[lineNum]
    #prints all 3 values
    def printInfo(self):
        print("Name: " + str(self.name))
        print("Phone: " + str(self.phoneNumber))
        print("Email: " + str(self.email))
    #prints in the format from the example
    def fullPrint(self):
        print("\nInput:\n\n" + self.fullBusinessCard + "\nOutput:\n")
        self.printInfo()
        print("")
#needed to ensure an email only has one .xxx ending (.com, .net ...)
def xor(a,b):
    #formal definition of xor
    return (a and not b) or (not a and b)
