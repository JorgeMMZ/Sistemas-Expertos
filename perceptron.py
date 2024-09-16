# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:11:51 2024

@author: Ghost
"""

import numpy as np
W = np.array([1,1,1])
Wn = W.copy()
x = np.array([[1,-1,-1],[1,1,-1],[1,-1,1],[1,1,1]])
y = np.array([-1,-1,-1,1])
yf = np.zeros(4)
for i in range (4):
    yp = np.sign(np.dot(Wn,x[i,:]))
    Wn = (Wn +(y[i]-yp)*(x[i,:])/2)
for i in range (4):
    yf[i] = np.sign(np.dot(Wn,x[i,:]))