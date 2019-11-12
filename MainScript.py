import numpy as np

menuItems = np.array(["Load data.","Filter data.","Display statistics.","Generate plots.","Quit."])
istheredata = False
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
        #bactnr = np.array(['1','2','3','4'])
        bactsortoption = np.array(["Salmonella Enterca","Bacillus Cereus","Listeria","Brochothrix Thermosphacta","Go back"])
        filtoptions = np.array(['Sort for Bacteria type.','Sort for Growth rate.','Go back'])
        option = displayMenu(filtoptions)
      
        
        if option == 1:
            #print("The bacteria must be one of the following: [1] Salmonella Enterica, [2] Bacillus Cereus, [3] Listeria or [4] Brochothrix Thermosphacta.")
            #bact_type = input("Please type a bacteria to sort for, for example type the number of the bacteria \"3\" or the name \"Listeria\" :")

            C = True
            D = True
            E = True
            F = True
            rowstack = np.array([])
            Temp,Growth,Bact = np.hsplit(data,3)
            bactnr = np.array([1,2,3,4])
            bactoption = displayMenu(bactsortoption)
            
            if bactoption == 1:
                
                for row in range(np.size(Growth)):
                    split = data[row,:]

                    if split[2] == bactnr[0]:
                        if D == False or E == False or F == False:
                            print("You have already sorted for another type of bacteria.")
                            pass
                        if C == True:
                            rowstack = split
                            C=False

                        else:
                            rowstack = np.vstack((rowstack,split))
            
            elif bactoption == 2:
                for row in range(np.size(Growth)):
                    split = data[row,:]

                    if split[2] == bactnr[1]:
                        if C == False or E == False or F == False:
                            print("You have already sorted for another type of bacteria.")
                            pass
                        if D == True:
                            rowstack = split
                            D=False

                        else:
                            rowstack = np.vstack((rowstack,split))
            

            
            
            elif bactoption == 3:
                
                for row in range(np.size(Growth)):
                    split = data[row,:]

                    if split[2] == bactnr[2]:
                        if C == False or D == False or F == False:
                            print("You have already sorted for another type of bacteria.")
                            pass
                        if E == True:
                            rowstack = split
                            E=False

                        else:
                            rowstack = np.vstack((rowstack,split))
            
       
            
            elif bactoption == 4:
                for row in range(np.size(Growth)):
                    split = data[row,:]

                    if split[2] == bactnr[3]:
                        if D == False or E == False or C == False:
                            print("You have already sorted for another type of bacteria.")
                            pass
                        if F == True:
                            rowstack = split
                            F=False

                        else:
                            rowstack = np.vstack((rowstack,split))
            elif bactoption == 5:
                pass
                            
            data = rowstack
            print(data)       

            
            
            
            
            
            
            
            
            
            
            
            
            
        if option == 2:
            #Lav og indsæt filter funktion, kunne være filter(growth_filter)
            
            upper = np.max(data) #upper og lower indtil vi andet er defineret
            lower = np.min(data)
            equal_true = False
            A=True
            B=True
            while True:
                growth_filter_option = np.array(["Set Upper Boundary","Set Lower Boundary","Set Equal = argument","Remove restrictions", "Finish"])
                growth_option = displayMenu(growth_filter_option)
                if growth_option == 1: #Upper boundary
                    #bla
                    upper = float(input("Type a upper boundary as a number: "))
                    assert upper > 0
                    assert upper > lower
                    
                    
                if growth_option == 2: #Lower boundary
                    #bla
                    lower = float(input("Type a lower boundary as a number: "))
                    assert lower < upper
                    
                if growth_option == 3: #Equal to
                    #bla    
                    equal = float(input("Type what the growth rate should be equal to: "))
                    equal_true = True
                if growth_option == 4: #Remove
                    data = dataLoad(filename) 
                    upper = np.max(data) #upper og lower indtil vi andet er defineret
                    lower = np.min(data)
                    equal_true = False
                if growth_option == 5: #Finish
                    #bla  
                    rowstack = np.array([])
                    Temp,Growth,Bact = np.hsplit(data,3)
                    if equal_true == True:
                        for row in range(np.size(Growth)):
                            split = data[row,:]

                            if split[1] == equal:
                                if B == False:
                                    print("You have already put an upper/lower restiction.")
                                    pass
                                if A == True:
                                    rowstack = split
                                    A=False

                                else:

                                    rowstack = np.vstack((rowstack,split))
                    elif equal_true == False:
                        for row in range(np.size(Growth)):
                            split = data[row,:]

                            if split[1]<upper and split[1]>lower:
                                if A == False:
                                    print("You have already put an equal restiction.")
                                    pass
                                if B == True:
                                    rowstack = split
                                    B = False

                                else:
                                    print(split,rowstack)
                                    rowstack = np.vstack((rowstack,split))
                                    

                    data = rowstack
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
        statslist = np.array(['Calculate the average temperature','Calculate the average growth rate','Calculate the standard deviation of the temperatures','Calculate standard deviation of the growth rates','Calculate the number of rows in the data','Calculate the average growth rate when the temperature is less than 20°C','Calculate the average growth rate when the temperature is greater than 50°C','Go back'])
        while True:
            statsoption = displayMenu(statslist)
            
            if statsoption == 1:
                stat = dataStatistics(data,1)
                print("The average temperature is {}".format(stat))
            elif statsoption == 2:
                stat = dataStatistics(data,2)
                print("The average growth rate is {}".format(stat))
            elif statsoption == 3:
                stat = dataStatistics(data,3)
                print("The standard deviation of the temperatures is {:.1f}".format(stat))
            elif statsoption == 4:
                stat = dataStatistics(data,4)
                print("The standard deviation of the growth rate is {:.2f}".format(stat))
            elif statsoption == 5:
                stat = dataStatistics(data,5)
                print("The data contains {} rows".format(stat))
            elif statsoption == 6:
                stat = dataStatistics(data,6)
                print("The average growth rate for temperatures smaller than 20°C is {}".format(stat))
            elif statsoption == 7: 
                stat = dataStatistics(data,7)
                print("The average growth rate for temperatures greater than 50°C is {}".format(stat))
            elif statsoption == 8:
                break
            
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
    