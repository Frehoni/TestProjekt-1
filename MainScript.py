import numpy as np

menuItems = np.array(["Load data.","Filter data.","Display statistics.","Generate plots.","Quit."])
while True:
    #Display menu
    choice = displayMenu(menuItems)
    # Enter filename
    istheredata = False
    if choice ==1:
        filename = input("Please enter the full file name, for example \"file.csv\" : ")
        data = dataLoad(filename)
        istheredata = True
    # Filter data
    elif choice == 2:
        if istheredata == False:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            data = dataLoad(filename)
            istheredata = True
        filtoptions = np.array(['Sort for Bacteria type.','Sort for Growth rate.','Go back'])
        option = displayMenu(filtoptions)
        if option == 1:
            print("The bacteria must be one of the following: [1] Salmonella Enterica, [2] Bacillus Cereus, [3] Listeria or [4] Brochothrix Thermosphacta.")
            bact_type = input("Please type a bacteria to sort for, for example type the number of the bacteria \"3\" or the name \"Listeria\" :")
        if option == 2:
            growth_filter = input("Type a range filter for the Growth rate, for example: \"0.5 < Growth_rate < 1\" :")
            #Lav og indsæt filter funktion, kunne være filter(growth_filter)
        if option == 3:
            pass
    # Display statistics
    elif choice ==3 :
        if istheredata == False:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            data = dataLoad(filename)
            istheredata = True
    #Generate plots
    elif choice == 4:
        if istheredata == False:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            data = dataLoad(filename)
            istheredata = True
    
    #Quit
    elif choice ==5:
        break
    