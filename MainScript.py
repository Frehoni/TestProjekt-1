import DataLoad
import inputnumber_and_displaymenu
import DataPlot
import numpy as np
menuItems =np.array(["Load data.","Filter data.","Display statistics.","Generate plots.","Quit."])
while True:
    #Display menu
    choice = displayMenu(menuItems)
    # Enter filename
    if choice ==1:
        filename = input("Please enter the full file name: ")
        data = dataLoad(filename)
    # Filter data
    elif choice == 2:
        print(name)
    # Display statistics
    elif choice ==3 :
        pass
    #Generate plots
    elif choice == 4:
        pass
    
    #Quit
    elif choice ==5:
        break
    