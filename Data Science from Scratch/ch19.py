# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:16:58 2017

@author: 2017041801
"""

import matplotlib.pyplot as plt
import random as rnd
import math
import numpy as np

def sum_of_distance(x,y):
    dist = []
    
    for i in range(len(x)):
        diff = np.array(x[i]) - np.array(y[i])
        dist.append(math.sqrt(np.dot(diff,diff)))
    
    return sum(dist)
    
def classify(inputs, means):
    classfier = {}
    
    for p in inputs:
        dist = []
        for i in range(len(means)):
            diff = np.array(p) - np.array(means[i])
            dist.append(math.sqrt(np.dot(diff,diff))) 
        classfier[inputs.index(p)] = str(dist.index(min(dist)) + 1)
    
    return classfier

def vector_mean(inputs):
    sum_x = 0
    sum_y = 0
    for p in inputs:
        sum_x += p[0]
        sum_y += p[1]
    return [sum_x / len(inputs), sum_y / len(inputs)]

def locate_means(k, inputs, classfier):
    group_means=[]
    for i in range(k):
        group = [inputs[ind] for ind, c in classfier.items() if c == str(i + 1)]
        group_means.append(vector_mean(group))
      
    return group_means
    
def kmeans(k, inputs):
    #initial group's center
    means = rnd.sample(inputs, k)
    pre_means = [[0,0] for _ in range(k)]
    
    while sum_of_distance(means, pre_means) > pow(10, -7):
        
        classfier = classify(inputs, means)
        pre_means = means
        means = locate_means(k, inputs, classfier)
       
    return (means, classfier)

inputs = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]
(means, classifier) = kmeans(2, inputs)

class_1=[]
class_2=[]
class_3=[]
for ind, c in classifier.items():
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
#xs_3 = [pair[0] for pair in class_3]
#ys_3 = [pair[1] for pair in class_3]

plt.plot(xs_1, ys_1, 'ro', xs_2, ys_2, 'go', #xs_3, ys_3, 'bo', \
         means[0][0], means[0][1], 'r^', \
         means[1][0], means[1][1], 'g^')#, \
         #means[2][0], means[2][1], 'b^')