import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
def dataPlot(data):
    
    Temp,Growth,Bact = np.hsplit(data,3)
    #Number of Bacteria plot
    bakterier,antal_bakterier = np.unique(Bact,return_counts=True)
    freq = np.asarray((bakterier,antal_bakterier))
    #https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-94.php
    SE, BC, L, BT = freq[0],freq[1],freq[2],freq[3]
    
    plt.title("Number of bacteria")
    plt.ylabel("Frequency of bacteria")
    plt.xlabel("Bacterias")
    plt.ylim([0, np.sum(freq)])
    plt.hist(freq,4,color='b',histtype='bar',ec='black')
    plt.show()
    #Growth rate by temperature plot
    plt.title("Growth rate of bacteria by temperature")
    plt.ylabel("Growth rate")
    plt.xlabel("Temperatures")
    plt.xlim([10, 60])
    plt.ylim([0, np.amax(Bact)])
    #create legend - https://stackoverflow.com/questions/43872450/matplotlib-histogram-with-multiple-legend-entries
    handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in [SE,BC,L,BT]]
    labels= ["[1] Salmonella Enterica","[2] Bacillus Cereus", "[3] Listeria","[4] Brochothrix Thermosphacta"]
    plt.legend(handles, labels)
    #plt.plot(y, x, color='b', label="Average temperature") 
    #plt.plot(y, xmean, color='r', label="Average Mean temperature")
    #plt.plot(y, x, color='b', label="Average temperature") 
    #plt.plot(y, xmean, color='r', label="Average Mean temperature")

    plt.show()

    

