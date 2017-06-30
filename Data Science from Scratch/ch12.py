# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 09:34:43 2017

@author: 2017041801
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def distance_by_target(labeled_p, new_p):
    by_distance = []
    for (x,y), lang in labeled_p:
        cord = [x,y]
        diff_by_new_p = np.array(new_p) - np.array(cord)
        distance_and_lang = (math.sqrt(np.dot(diff_by_new_p,diff_by_new_p)), lang)
        by_distance.append(distance_and_lang)
    return by_distance    

def sorted_tuple(k, labeled_p, target_p):
    distance_of_points = distance_by_target(labeled_p, target_p) #計算各點與測試點的距離
    sort_list = []
    lang_list = []
    count = 0
    for d,lang in distance_of_points:
        if count < k: #建立一個list，有k各項目
            sort_list.append(d)
            lang_list.append(lang)
            count += 1
            continue
        if d < max(sort_list): #找出前k大
            ind = sort_list.index(max(sort_list))
            sort_list[ind] = d
            lang_list[ind] = lang
    return sort_list,lang_list

def confirm_category(k, type_list): #確認所屬類別
    counter = Counter(type_list)
    ini_max = 0.000001
    outcome = 'unclassify'
    for k, v in counter.items():
        if ini_max < v:
           outcome = k
           ini_max = v
    return outcome

def knn_classify(k, labeled_p, target_p):
    dist_list,lang_list = sorted_tuple(k, labeled_p, target_p)
    outcome = confirm_category(k, lang_list)
    
    plt.plot(target_p[0], target_p[1], 'c*')
    return outcome,[(x,y) for (x,y) in zip(dist_list,lang_list)]
    

cities = [([-122.3, 47.53], 'Python'),
          ([-96.85, 32.85], 'Java'),
          ([-89.33, 43.13], 'R'),
          ([-115.2, 39.6], 'Python'),
          ([-91.85, 33.85], 'Java'),
          ([-108.3, 44], 'Python'),
          ([-102.85, 35.85], 'Java'),
          ([-100, 43.13], 'R'),
          ([-113.2, 34.6], 'Python'),
          ([-105.5, 35.85], 'Java'),
          ([-110.9, 42.5], 'Java'),
          ([-94, 46.13], 'R')]

plots= {'Python':([],[]), 'Java':([],[]), 'R':([],[])}
markers = {'Python':'o', 'Java':'^', 'R':'s'}
colors = {'Python':'r', 'Java':'g', 'R':'b'}

for (cord_x,cord_y), k in cities:
    plots[k][0].append(cord_x)
    plots[k][1].append(cord_y)
    
for k, (x, y) in plots.items():
    plt.scatter(x, y, color=colors[k], marker=markers[k], label=k)
    plt.legend(loc=3)
    plt.axis([-130,-80,30,50])
    
print(knn_classify(5, cities, (-95,40)))    