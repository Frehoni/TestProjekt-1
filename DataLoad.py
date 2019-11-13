import numpy as np
import pandas as pd


def dataLoad(filename):

    try: #Tjekker om filen kan findes og kan læses
        fildata = pd.read_csv(filename) #Åbner og læser filen så den kan bruges
    except FileNotFoundError:
        return "Date file not found, please try again"
    Temperature = np.array([]) #Tre åbne vektorerer til data
    Growth = np.array([])
    Bacteria = np.array([])
    Bactnr = np.array([1,2,3,4])
    if errormsg == True:
        print("Error report:")
    for i in range(len(fildata.Temperature)): #Laver et loop for antallet af data rækker
        if fildata.Temperature[i]<10 or fildata.Temperature[i]>60 or fildata.Growth_rate[i]<0 or fildata.Bacteria[i] not in Bactnr : #Verdens længste if-statement der tjekker om alle kravene gælder
            if errormsg == True:
                if fildata.Temperature[i]<10 or fildata.Temperature[i]>60:
                    print("Error at test {}, the temperature is {}°C: Temperature has to be between 10°C and 60°C.".format(i,fildata.Temperature[i]))
                if fildata.Growth_rate[i]<0:
                    print("Error at test {}, the growth rate is {}: Growth rate must be a positive number.".format(i,fildata.Growth_rate[i]))
                if fildata.Bacteria[i] not in Bactnr:
                    print("Error at test {}, the bacteria is [{}]-Unknown: The bacteria must be either [1],[2],[3] or [4] ".format(i,fildata.Bacteria[i]))
        else: #Samler den godkendte data
            Tem=fildata.Temperature[i]
            Temperature = np.append(Temperature,Tem)
            Gro=fildata.Growth_rate[i]
            Growth = np.append(Growth,Gro)
            Bac=fildata.Bacteria[i]
            Bacteria = np.append(Bacteria,Bac)
    data = np.column_stack((Temperature,Growth,Bacteria)) #Samler den godkendte data i en Nx3 matrice
    return data

#print(dataLoad("random.csv"))
        
        
        