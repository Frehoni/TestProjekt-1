# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:53:34 2019

@author: Anton
"""
import numpy as np
A = np.column_stack((np.array([12,50,30]),np.array([1.1,0.2,1]),np.array([2,4,1])))
print(A[1,:])

b = A[1,:]
c = A[2,:]
print(np.vstack((b,c)))

print('juhhuuu')
for i in range(3):
    b=np.vstack((b,c))
    
print(b)