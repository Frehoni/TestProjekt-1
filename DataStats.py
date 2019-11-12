import numpy as np


def dataStatistics(data,statistic):
    #options = np.array(['mean temperature','mean growth rate','std temperature','std growth rate','rows','mean cold growth rate','mean hot growth rate'])
    Temp,Growth,Bact = np.hsplit(data,3)
    if statistic == 1: #Mean Temperature
        result = np.mean(Temp)
        return result
    elif statistic == 2: #Mean Growth Rate
        result = np.mean(Growth)
        return result
    elif statistic ==  3: #Std Temperature
        result = np.std(Temp)
        return result
    elif statistic == 4: #Std Growth Rate
        result = np.std(Growth)
        return result
    elif statistic == 5: #Rows
        result = np.size(Temp)
        return result
    elif statistic == 6: #Mean Cold Growth rate
        
        less = data[np.where(data[:,0] < 20)]
        n1,g20,n2 = np.hsplit(less,3)
        result = np.mean(g20)
        return result
    
    elif statistic == 7: #Mean Hot Growth rate
        great = data[np.where(data[:,0] > 40)]
        n1,g50,n2 = np.hsplit(great,3)
        result = np.mean(g50)
        return result

    
