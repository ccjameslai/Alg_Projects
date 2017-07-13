# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:16:58 2017

@author: 2017041801
"""

import matplotlib.pyplot as plt
import random as rnd
import math
import numpy as np

def distance_sum(x,y):
    dist = []
    for i in range(len(x)):
        diff = np.array(x[i]) - np.array(y[i])
        dist.append(math.sqrt(np.dot(diff,diff)))
    
    return sum(dist)
    
    
def kmeans(k, inputs):
    #initial group's center
    means = rnd.sample(inputs, k)
    pre_means = [[0,0], [0,0], [0,0]]
    
    while distance_sum(means, pre_means) > pow(10, -7):
        pre_means = means
        #calculate distance of each point to centers
        classfier = {}
        for p in inputs:
            dist = []
            for i in range(len(means)):
                diff = np.array(p) - np.array(means[i])
                dist.append(math.sqrt(np.dot(diff,diff))) 
            classfier[inputs.index(p)] = str(dist.index(min(dist)) + 1)
            
        class_1=[]
        class_2=[]
        class_3=[]
        for ind, c in classfier.items():
            if c == '1':
                class_1.append(inputs[ind])
            elif c == '2':
                class_2.append(inputs[ind])
            else:
                class_3.append(inputs[ind])
        
        xs_1 = [pair[0] for pair in class_1]
        ys_1 = [pair[1] for pair in class_1]
        xs_2 = [pair[0] for pair in class_2]
        ys_2 = [pair[1] for pair in class_2]
        xs_3 = [pair[0] for pair in class_3]
        ys_3 = [pair[1] for pair in class_3]
        
        c1_mean = [sum(xs_1) / len(xs_1), sum(ys_1) / len(ys_1)]
        c2_mean = [sum(xs_2) / len(xs_2), sum(ys_2) / len(ys_2)]
        c3_mean = [sum(xs_3) / len(xs_3), sum(ys_3) / len(ys_3)]
    
        means = [c1_mean, c2_mean, c3_mean]
           
    plt.plot(xs_1, ys_1, 'ro', xs_2, ys_2, 'go', xs_3, ys_3, 'bo')
    
    return classfier

inputs = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]
c = kmeans(3, inputs)
print(c)