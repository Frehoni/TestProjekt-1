import numpy as np


def dataStatistics(data,statistic):
    options = np.array(['mean temperature','mean growth rate','std temperature','std growth rate','rows','mean cold growth rate','mean hot growth rate'])
    Temp,Growth,Bact = np.hsplit(data,3)
    if statistic.lower() == options[0]: #Mean Temperature
        result = np.mean(Temp)
        return result
    if statistic.lower() == options[1]: #Mean Growth Rate
        result = np.mean(Growth)
        return result
    if statistic.lower() == options[2]: #Std Temperature
        result = np.std(Temp)
        return result
    if statistic.lower() == options[3]: #Std Growth Rate
        result = np.std(Growth)
        return result
    if statistic.lower() == options[4]: #Rows
        result = np.size(Temp)
        return result
    if statistic.lower() == options[5]: #Mean Cold Growth rate
        result = np.mean(Temp[Temp<20])
        return result
    if statistic.lower() == options[6]: #Mean Hot Growth rate
        result = np.mean(Temp[Temp>50])
        return result
    
    
