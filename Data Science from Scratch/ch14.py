# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:50:16 2017

@author: 2017041801
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def difference_with_mean(x):
    return np.array(x) - (sum(x) / len(x)) * np.ones(len(x))

def least_square(x,y):
    diff_with_mx = difference_with_mean(x)
    diff_with_my = difference_with_mean(y)
        
    x_bar = (sum(x) / len(x))
    y_bar = (sum(y) / len(y))
    beta = np.dot(diff_with_mx, diff_with_my) / np.dot(diff_with_mx, diff_with_mx)
    alpha = y_bar - beta * x_bar
    
    return (alpha, beta)

def sum_of_error(x,y,alpha,beta):
    return sum(np.array(y) - alpha * np.ones(len(y)) - beta * np.array(x))

def gradient(x,y,alpha=0, beta=0, rate=-0.001):
    iter_num = 0
    
    while sum_of_error(x,y,alpha,beta) > 1:
        gradien_alpha = -2 * sum_of_error(x,y,alpha,beta) / len(y)
        gradien_beta = -2 * np.dot((np.array(y) - alpha * np.ones(len(y)) - beta * np.array(x)), x) / len(y)
    
        new_alpha = alpha + rate * gradien_alpha
        new_beta = beta + rate * gradien_beta
        
        #min_value = sum_of_error(x,y,new_alpha,new_beta)
        iter_num += 1
        alpha, beta = new_alpha, new_beta
           
    return (alpha, beta, iter_num)


num_friends_good = [49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
daily_minutes_good = [68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

#plt.plot(num_friends_good, daily_minutes_good, 'bo')

least_square(num_friends_good, daily_minutes_good)
alpha, beta, iter_num = gradient(num_friends_good, daily_minutes_good)
print(alpha, beta, iter_num)
