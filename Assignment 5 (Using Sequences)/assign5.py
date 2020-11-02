#ENGI 1020 - Assignment 5; Umama Rahman; ID: 202000915

number = int(input("How many words? "))

wordList = []

for i in range(number):
    word = input("Word? ")
    wordList += [word]
    
longestWord = " "
longestLen = 0

for word in wordList:
    if (longestLen < len(word)):
        longestLen = len(word)
        longestWord = word
        
print("Longest word:", longestWord)

firstLetters = ""

for word in wordList:
    firstLetters += word[0]
    
print("First letters:", firstLetters)



    
    

    
