###The below function accepts a sentence as a string and determines whether it is valid based on the below criteria:###
###1. String starts with a capital letter.###
###2. String has an even number of quotation marks.###
###3. String ends with one of the following sentence termination characters: ".", "?", "!"###
###4. String has no period characters other than the last character.###
###5. Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).###

import re #regular expressions python library
import os

def sentenceChecker(checkedString):
    #The main function creates an empty list and appends all the above function tests to it as booleans. 
    # If any of the items on the list are false, function returns false, otherwise true.
    testsList = []
    if checkedString: #Making sure the string isn't empty
        testsList.append(True if re.search("^[A-Z]",checkedString) else False) #Using reguar expressions to test if string starts with capital letter
        testsList.append(True if re.search("[.,?,!]$",checkedString) else False) #Using reguar expressions to test if string ends with any of the approved termination characters
        testsList.append(len(re.findall(r'\"', checkedString))%2 == 0) #Using regular expressions to list all quotation marks, then using the modulo operator on the length of the list to test if it's even
        testsList.append(not re.findall(r"\.", checkedString[:-1])) #Using regular expressions to test if there are any '.' in all but the last character of the string.
        testsList.append(not any(int(num) < 13 for num in re.findall(r'\d+', checkedString))) #using the re.findall method to test the string for any numbers, then return false if any are below 13
        if testsList.count(False) > 0: #if none of the above tests are false, user gets notification that their string is valid, otherwise notified invalid
            return False
        else:
            return True
    else:
        print('Empty sentence submitted, please try again.')

if __name__ == "__main__":
    looper = True
    while looper == True:
        os.system('CLS') #clears the console, keeping it nice and clean for the user
        inputSentence = input('Please submit the sentence you wish to check here: ') #user input
        if sentenceChecker(inputSentence): #run the checker function
            print('Sentence is valid!')
        else:
            print('Sentence is invalid')
        while True: 
            #using an additional while loop as I need to look for three states of the input- 'y', 'n' and any other character. 
            #When the user select 'n' for not wanting to continue, the looper variable turns false and the nested while loop break, causing the function to stop
            #a 'y' answer breaks the nested while loop but not the outer while loop, continuing the sentence checking
            #any other character gives the user an error message and asks them again
            continueTest = input('Would you like to check additional sentences? y/n: ') #checking if user wants to continue
            if continueTest == 'n':
                os.system('CLS')
                looper = False
                break
            elif continueTest == 'y':
                break
            else:
                print('Invalid character submitted, please try again!')
                continue
