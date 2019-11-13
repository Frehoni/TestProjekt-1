import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data):
    
    Temp,Growth,Bact = np.hsplit(data,3)
    #Number of Bacteria plot
    #Sorterer for talene 1,2,3 og 4. Tæller derefter antallet af de tal.
    bakterier,antal_bakterier = np.unique(Bact,return_counts=True)
    freq = np.asarray(antal_bakterier)
    #https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-94.php
    b = 0
    if 1 in bakterier:
        SE = freq[b]
        b=b+1
    else:
        SE = 0
    if 2 in bakterier:
        BC = freq[b]
        b=b+1
    else:
        BC = 0
    if 3 in bakterier:
        L = freq[b]
        b=b+1
    else:
        L = 0
    if 4 in bakterier:
        BT = freq[b]
    else:
        BT = 0
    #https://python-graph-gallery.com/3-control-color-of-barplots/
    #https://matplotlib.org/tutorials/introductory/pyplot.html
    freq = np.array([SE,BC,L,BT])
    navne = ['[1] SE','[2] BC','[3] L','[4] BT']
    plt.bar(navne,freq, color= ['red','green','blue','cyan'])
    plt.title("Number of bacteria")
    plt.ylabel("Frequency of bacteria")
    plt.xlabel("Bacterias")
    print("Printed plots: ")
    plt.show()
    #Growth rate by temperature plot
    #Data for Salmonella
    salmo = data[np.where(data[:,2] == 1)]
    x1 = np.sort(salmo[:,0])
    y1 = np.sort(salmo[:,1])
    
    plt.plot(x1,y1,color='red',label="Salmonella Enterca")
    #Data for Bacillus cereus
    bakt2 = data[np.where(data[:,2] == 2)]
    x2 = np.sort(bakt2[:,0])
    y2 = np.sort(bakt2[:,1])
    plt.plot(x2,y2,color='green',label="Bacillus Cereus")
    #Data for Listeria
    bakt3 = data[np.where(data[:,2] == 3)]
    x3 = np.sort(bakt3[:,0])
    y3 = np.sort(bakt3[:,1])
    plt.plot(x3,y3,color='blue',label="Listeria")
    #Data for Brochothrix Thermosphacta
    bakt4 = data[np.where(data[:,2] == 4)]
    x4 = np.sort(bakt4[:,0])
    y4 = np.sort(bakt4[:,1])
    plt.plot(x4,y4,color='cyan',label="Brochothrix Thermosphacta")
    #Generelt for Plot
    plt.title("Growth rate of bacteria by temperature")
    plt.ylabel("Growth rate")
    plt.xlabel("Temperatures")
    plt.xlim([10, 60])
    plt.ylim([0, np.amax(Growth)+0.5])
    plt.legend(loc="upper left")
    plt.show()

