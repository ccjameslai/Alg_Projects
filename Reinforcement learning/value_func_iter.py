# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:50:44 2018

@author: James
"""

states = [s for s in range(0,16)]
values = [0] * 16
r = -1
policy = 0.25

for k in range(10):
    temp_values = [0] * 16
    for i in range(len(values)):
        if i == 0:
            continue
        if i == 15:
            break
        if (i >= 1) and (i <= 2):
            temp_values[i] = policy * (r+values[i]) + policy * (r+values[i - 1]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i + 4])
        elif i == 3:
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i]) \
            + policy * (r+values[i]) + policy * (r+values[i + 4])
        elif  (i == 4) or (i == 8):
            temp_values[i] = policy * (r+values[i - 4]) + policy * (r+values[i]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i + 4])
        elif (i == 5) or (i == 6) or (i == 9) or (i == 10):
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i + 4])
        elif (i == 7) or (i == 11):
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i]) + policy * (r+values[i + 4])
        elif i == 12:
            temp_values[i] = policy * (r+values[i]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i])
        else:
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i])
            
    values = temp_values
print(values)