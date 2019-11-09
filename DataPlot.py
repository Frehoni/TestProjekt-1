import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
def dataPlot(data):
    
    Temp,Growth,Bact = np.hsplit(data,3)
    #Number of Bacteria plot
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

    plt.show()
    #Growth rate by temperature plot
    plt.title("Growth rate of bacteria by temperature")
    plt.ylabel("Growth rate")
    plt.xlabel("Temperatures")
    plt.xlim([10, 60])
    plt.ylim([0, np.amax(Growth)])
    #create legend - https://stackoverflow.com/questions/43872450/matplotlib-histogram-with-multiple-legend-entries
    #handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in [SE,BC,L,BT]]
    #labels= ["[1] Salmonella Enterica","[2] Bacillus Cereus", "[3] Listeria","[4] Brochothrix Thermosphacta"]
    #plt.legend(handles, labels)"""
    #plt.plot(y, x, color='b', label="Average temperature") 
    #plt.plot(y, xmean, color='r', label="Average Mean temperature")
    #plt.plot(y, x, color='b', label="Average temperature") 
    #plt.plot(y, xmean, color='r', label="Average Mean temperature")

#print(dataPlot(np.column_stack((np.array([12,50,30]),np.array([1.1,0.2,1]),np.array([2,4,1]))))) 


