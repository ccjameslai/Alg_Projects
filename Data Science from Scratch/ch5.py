# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:24:18 2017

@author: 2017041801
"""

from collections import Counter
import numpy as np
import math
from matplotlib import pyplot as plt

def mean(x):
    return sum(x) / len(x)

def de_mean(x, fn = mean):
    x_bar = fn(x)
    return [x_i - x_bar for x_i in x]

def median(v):
    n = len(v)
    s_v = sorted(v)
    midpoint = n // 2
        
    if n%2 == 0:
        return (s_v[midpoint - 1] + s_v[midpoint]) / 2
    else:
        return s_v[midpoint]

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    counter = Counter(x)
    max_v = max(counter.values())
    return [k for k,v in counter.items() if v == max_v]

def variance(x):
    sqr_de_mean = sum(np.array(de_mean(x)) * np.array(de_mean(x)))
    return sqr_de_mean / (len(x) - 1)
    
def covariance(x,y):
    return np.dot(de_mean(x), de_mean(y)) / (len(x) - 1)

def std(x):
    return math.sqrt(variance(x))

def correlation(x,y):
    return covariance(x,y) / (std(x) * std(y))
    
x = [1,1,1,2,3,4,4,4,5,6]
y = [1,4,1,8,3,4,9,4,5,6]
print(de_mean(x,mean))
print(quantile(x,0.75))
print(mode(x))
print(variance(x))
print(std(x))
print(covariance(x,x))
print(correlation(x,x))

plt.scatter(x,x)










