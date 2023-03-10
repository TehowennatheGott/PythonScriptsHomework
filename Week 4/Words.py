trueFalse = True

wordList = set()

while trueFalse:
    words = input("Please Enter a Word, or 'Show' to show all current words. \nYou can also say 'Exit' to exit the program\n")
    if words == "Show" or words == "show":
        print(wordList)
    elif words == "Exit" or words == "exit":
        trueFalse = False
    elif words.isdigit():
        print("Sorry, no numbers")
    elif words not in wordList:
        print("Added")
        wordList.add(words)
    elif words in wordList:
        print ("Already in word list")
        
    
