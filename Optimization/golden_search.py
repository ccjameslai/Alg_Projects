# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 09:30:50 2017

@author: 2017041801
"""
import pylab as plt

def func(x):
    c = x - 3
    return 2*pow(c,2) - 6

def golden_search(func, lower, upper, alpha = 0.382, e = pow(10, -6)):
    extrem = alpha * (upper - lower) + lower
    while upper - lower > e:
        d = upper - alpha * (upper - lower)
        if func(d) > func(extrem):
            upper = d
        else:
            lower = extrem
            extrem = d    
    return extrem

e = golden_search(func, -10,10)
x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
f = [func(i) for i in x]
plt.plot(x, f,'b', e, func(e), 'ro')
