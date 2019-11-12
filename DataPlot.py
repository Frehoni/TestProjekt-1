import numpy as np
import matplotlib.pyplot as plt

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
<<<<<<< HEAD
=======
    #Data for Salmonella
    salmo = data[np.where(data[:,2] == 1)]
    x1 = np.sort(salmo[:,0])
    y1 = np.sort(salmo[:,1])
    
    print(x1,y1)
    plt.plot(x1,y1,color='red',legend="Salmonella Enterca")
    #Data for bakterie 2
    bakt2 = data[np.where(data[:,2] == 2)]
    x2 = np.sort(bakt2[:,0])
    y2 = np.sort(bakt2[:,1])
    plt.plot(x2,y2,color='green',legend="Bacillus Cereus")
    #Data for bakterie 3
    bakt3 = data[np.where(data[:,2] == 3)]
    x3 = np.sort(bakt3[:,0])
    y3 = np.sort(bakt3[:,1])
    plt.plot(x3,y3,color='blue',legend="Listeria")
    #Data for bakterie 4
    bakt4 = data[np.where(data[:,2] == 4)]
    x4 = np.sort(bakt4[:,0])
    y4 = np.sort(bakt4[:,1])
    plt.plot(x4,y4,color='cyan',legend="Brochothrix Thermosphacta")
    #Generelt for Plot
>>>>>>> 93ad4a123c19f2a747942015beba73ab460e802e
    plt.title("Growth rate of bacteria by temperature")
    plt.ylabel("Growth rate")
    plt.xlabel("Temperatures")
    plt.xlim([10, 60])
    plt.ylim([0, np.amax(Growth)])
<<<<<<< HEAD
=======
    plt.legend(loc="upper left")
    plt.show()
>>>>>>> 93ad4a123c19f2a747942015beba73ab460e802e
    #create legend - https://stackoverflow.com/questions/43872450/matplotlib-histogram-with-multiple-legend-entries
    #handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in [SE,BC,L,BT]]
    #labels= ["[1] Salmonella Enterica","[2] Bacillus Cereus", "[3] Listeria","[4] Brochothrix Thermosphacta"]
    #plt.legend(handles, labels)"""
    #plt.plot(y, x, color='b', label="Average temperature") 
    #plt.plot(y, xmean, color='r', label="Average Mean temperature")
    #plt.plot(y, x, color='b', label="Average temperature") 
    #plt.plot(y, xmean, color='r', label="Average Mean temperature")

print(dataPlot(np.column_stack((np.array([12,50,30]),np.array([1.1,0.2,1]),np.array([2,4,1]))))) 

"""plt.title("Mean temperatures in the UK")
plt.ylabel("Mean temperaturs (degree Celcius)")
plt.xlabel("Year")
plt.xlim([1920, 2010])
plt.ylim([7.0, 10.5])
plt.plot(y, x, color='b', label="Average temperature") 
plt.plot(y, xmean, color='r', label="Average Mean temperature") 
plt.legend(loc="upper left")
savefig(plot, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()"""
