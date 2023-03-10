trueFalse = True

guestList = set()
confirmList = set()
notguestList = set()

while trueFalse:
    guest = input("Please Enter a guest, or 'Show' to show the amount of current guests. \nEnter 'Change' to change a guests invitation status. \nYou can also say 'Exit' to exit the program\n")
    if guest == "Show" or guest == "show":# Display how many people have been invited to the party, how many confirmed, and how many canceled
        print(len(guestList),"Guests invited")
        print(len(confirmList),"Guests confirmed")
        print(len(notguestList),"Guests cancelled")
    elif guest == "Exit" or guest == "exit":#Exit the program
        trueFalse = False
    elif guest == "Change" or guest == "change":#change a guests invite status
        changing = True
        while changing:
            print("Guests invited",guestList)
            print("Guests cancelled",notguestList)
            print("Guests confirmed", confirmList)
            guest = input("Which guest would you like to change? \n'Exit' to leave this window \n")
            if guest in guestList:
                yesno = input("Are they coming? Y/N\n")
                if yesno == "N":#if no confirm/cancallation, remove from confirms
                    notguestList.add(guest)
                    if guest in confirmList:#checks to see if they were confirmed
                        confirmList.remove(guest)
                    print("Removed")
                elif yesno == "Y":#if confirmed, add them to list and remove from notguestlist
                    print("added as confimed")
                    confirmList.add(guest)
                    if guest in notguestList:
                        notguestList.remove(guest)
                else:# only takes Y/N
                    print("Choose either Y/N")
            elif guest == "Exit" or guest == "exit":#Exits from this window to go back to adding people
                changing = False
            elif guest not in guestList:#if they aint on the list
                print("Not in List")
    elif guest.isdigit():#exception handling
        print("Sorry, no numbers")
    elif guest not in guestList:#if they aint on the list
        print("Added")
        guestList.add(guest)
    elif guest in guestList:#if they on the list
        print ("Already in list")