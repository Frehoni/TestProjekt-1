import numpy as np

menuItems = np.array(["Load data.","Filter data.","Display statistics.","Generate plots.","Quit."])
while True:
    #Display menu
    choice = displayMenu(menuItems)
    # Enter filename

    if choice ==1:
        filename = input("Please enter the full file name, for example \"file.csv\" : ")
        data = dataLoad(filename)
        istheredata = True
    # Filter data
    elif choice == 2:
        if istheredata != True:
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
            #Lav og indsæt filter funktion, kunne være filter(growth_filter)
            
            upper = np.max(data) #upper og lower indtil vi andet er defineret
            lower = np.min(data)
            equal_true = False
            growth_filter_option = np.array(["Set Upper Boundary","Set Lower Boundary","Set Equal = argument","Remove restrictions", "Finish"])
            growth_option = displayMenu(growth_filter_option)
            growth_filter = input("Please select an option: ")
            while True:
                
                if growth_option == 1: #Upper boundary
                    #bla
                    upper = input("Type a upper boundary as a number: ")
                    assert upper < 0
                    assert upper > lower
                    
                    
                if growth_option == 2: #Lower boundary
                    #bla
                    lower = input("Type a lower boundary as a number: ")
                    assert lower < upper
                    
                if growth_option == 3: #Equal to
                    #bla    
                    equal = input("Type what the growth rate should be equal to: ")
                    equal_true = True
                if growth_option == 4: #Remove
                    data = dataLoad(filename) 
                    upper = np.max(data) #upper og lower indtil vi andet er defineret
                    lower = np.min(data)
                    equal_true = False
                if growth_option == 5: #Finish
                    #bla  
                    colomnstack = np.array([])
                    Temp,Growth,Bact = np.hsplit(data,3)
                    if equal_true == True:
                        for colmn in range(np.size(Growth)):
                            split = np.vsplit(data,[colmn])
                            if split[1] == equal:
                                colomnstack = np.column_stack(colomnstack,split)
                    else:
                        for colmn in range(np.size(Growth)):
                            split = np.vsplit(data,[colmn])
                            if split[1] < upper and split[1] > lower:
                                colomnstack = np.column_stack(colomnstack,split)

                    break
                
            
        if option == 3:
            pass
    # Display statistics
    elif choice ==3 :
        if istheredata != True:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            data = dataLoad(filename)
            istheredata = True
    #Generate plots
    elif choice == 4:
        if istheredata != True:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            data = dataLoad(filename)
            istheredata = True
    
    #Quit
    elif choice ==5:
        break
    