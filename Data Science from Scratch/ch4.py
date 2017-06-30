# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:17:58 2017

@author: 2017041801
"""

import numpy as np
import math

def is_diagonal(m):
    for i in range(len(m) - 1):
        for j in range(len(m) - i - 1):
            if m[i][i + j + 1] != m[i + j + 1][i]:
                return 0
    return 1

d = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

dd = np.array([[1,2,3],
               [2,5,6],
               [3,6,9]])
    
    
v = np.array([[1,2,3],
             [4,5,6]])

w = np.array([[1,2],
             [3,4],
             [5,6]])
    
v_w = v + w
s_vw = sum(v_w)
d_vm = v.dot(w)
sq = math.sqrt((v-w).dot((v-w)))

print(is_diagonal(dd))