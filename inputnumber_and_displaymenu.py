def inputNumber(prompt):
    #Inputnumber pronts user to input a number
    #
    #Usage: num=inputNumber(promt) Displays promt and asks user for a number.
    #Repeats until user inputs a valid number.
    
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num

def displayMenu(options):
    #DisplayMenu displays a menu of options, ask the user to choose an number
    #and returns the number of the menu item chosen.
    #
    #Usage: choice = displayMenu(options)
    #
    #Input options Menu options (cell array of strings)
    #Output choice Chosen option (integer)
    
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1,options[i]))
        
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice