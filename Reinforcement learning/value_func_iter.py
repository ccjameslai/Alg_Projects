# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:50:44 2018

@author: James
"""

def policy_evaluation(values,r,policy):
    temp_values = [0] * 16
    for i in range(len(values)):
        if i == 0:
            continue
        if i == 15:
            break
        if (i >= 1) and (i <= 2):
            temp_values[i] = policy * (r+values[i]) + policy * (r+values[i - 1]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i + 4])
            temp_values[i] = round(temp_values[i],1)
        elif i == 3:
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i]) \
            + policy * (r+values[i]) + policy * (r+values[i + 4])
            temp_values[i] = round(temp_values[i],1)
        elif  (i == 4) or (i == 8):
            temp_values[i] = policy * (r+values[i - 4]) + policy * (r+values[i]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i + 4])
            temp_values[i] = round(temp_values[i],1)
        elif (i == 5) or (i == 6) or (i == 9) or (i == 10):
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i + 4])
            temp_values[i] = round(temp_values[i],1)
        elif (i == 7) or (i == 11):
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i]) + policy * (r+values[i + 4])
            temp_values[i] = round(temp_values[i],1)
        elif i == 12:
            temp_values[i] = policy * (r+values[i]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i])
            temp_values[i] = round(temp_values[i],1)
        else:
            temp_values[i] = policy * (r+values[i - 1]) + policy * (r+values[i - 4]) \
            + policy * (r+values[i + 1]) + policy * (r+values[i])
            temp_values[i] = round(temp_values[i],1)
    return temp_values

def policy_improvement(values,r):
    pi = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'11':[],'12':[],'13':[],'14':[]}
    actions = ['<','^','>', 'v']
    for i in range(len(values)):
        if i == 0 or i == 15:
            continue
        if (i >= 1) and (i <= 2):
            temp = [(r+values[i - 1]), (r+values[i]) ,(r+values[i + 1]) ,(r+values[i + 4])]
            pi[str(i)] = actions[temp.index(max(temp))]
        elif i == 3:
            temp = [(r+values[i - 1]), (r+values[i]) ,(r+values[i]) ,(r+values[i + 4])]
            pi[str(i)] = actions[temp.index(max(temp))]
        elif  (i == 4) or (i == 8):
            temp = [(r+values[i]),(r+values[i - 4]),(r+values[i + 1]),(r+values[i + 4])]
            pi[str(i)] = actions[temp.index(max(temp))]            
        elif (i == 5) or (i == 6) or (i == 9) or (i == 10):
            temp = [(r+values[i - 1]),(r+values[i - 4]) ,(r+values[i + 1]),(r+values[i + 4])]
            pi[str(i)] = actions[temp.index(max(temp))]    
        elif (i == 7) or (i == 11):
            temp = [(r+values[i - 1]),(r+values[i - 4]) ,(r+values[i]),(r+values[i + 4])]
            pi[str(i)] = actions[temp.index(max(temp))]
        elif i == 12:
            temp = [(r+values[i]),(r+values[i - 4]),(r+values[i + 1]),(r+values[i])]
            pi[str(i)] = actions[temp.index(max(temp))]
        else:
            temp = [(r+values[i - 1]) ,(r+values[i - 4]) ,(r+values[i + 1]),(r+values[i])]
            pi[str(i)] = actions[temp.index(max(temp))]
    return pi        

values = [0] * 16
r = -1
policy = 0.25

for k in range(10):
    values = policy_evaluation(values,r,policy)
    pi = policy_improvement(values,r)
print(pi)