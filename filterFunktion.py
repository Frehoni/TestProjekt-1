
#def filterFunction(data,userinput):
    




import numpy as np

g = np.array([1,2,3,4,5,6])

b = 'g[g<3]'

a = exec('g[g<3]',globals(),locals())

print(a)