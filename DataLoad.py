import numpy as np
import pandas as pd

def dataLoad(filename):
    errormsg = True #Skal man spammes med errormsg eller ej. Måske et input fra brugeren?
    fildata = pd.read_csv(filename) #Åbner og læser filen
    Temperature = np.array([]) #Tre åbne vektorerer til data
    Growth = np.array([])
    Bacteria = np.array([])
    for i in range(len(fildata.Temperature)): #Laver et loop for antallet af data rækker
        if fildata.Temperature[i]<10 or fildata.Temperature[i]>60 or fildata.Growth_rate[i]<0 or fildata.Bacteria[i]<1 or fildata.Bacteria[i]>4 : #Verdens længste if-statement der tjekker om alle kravene gælder
            if errormsg == True:
                if fildata.Temperature[i]<10 or fildata.Temperature[i]>60:
                    print("Error at test {} , the temperature is {}: Temperature is not in accepted range".format(i,fildata.Temperature[i]))
                if fildata.Growth_rate[i]<0:
                    print("Error at test {}, the growth rate is {}: Growth rate must be a positive number".format(i,fildata.Growth_rate[i]))
                if fildata.Bacteria[i]<1 or fildata.Bacteria[i]>4:
                    print("Error at test {}, the bacteria is {}: The bacteria must be one of the following: [1] Salmonella, [2] Sacillus sereus, [3] Listeria or [4] Brochothrix Thermosphacta".format(i,fildata.Bacteria[i]))
        else: #Samler den godkendte data
            Tem=fildata.Temperature[i]
            Temperature = np.append(Temperature,Tem)
            Gro=fildata.Growth_rate[i]
            Growth = np.append(Growth,Gro)
            Bac=fildata.Bacteria[i]
            Bacteria = np.append(Bacteria,Bac)
    data = np.column_stack((Temperature,Growth,Bacteria)) #Samler den godkendte data i en Nx3 matrice
    return data

print(dataLoad('random.csv'))
        
        
        
        