import Kmeans
import random as rnd
import numpy as np
import math
from matplotlib import pyplot as plt

def Test_distance():
    kmeans = Kmeans.kmeans()

    p=[1,2,3,4]
    dist_set = kmeans.distance(p)
    print(dist_set)
    print('len dist_set', len(dist_set))

#Test_distance()

def Test_arrangement():
    kmeans = Kmeans.kmeans()
    xdata = kmeans.gen_xdata()
    p_set = []
    for i in range(3):
        indx = rnd.randint(0, len(xdata))
        p_set.append(xdata[indx])
    print('p_set', p_set)
    dist_in_group = {}
    for index, p in enumerate(p_set):
        dist_set = kmeans.distance(p)
        dist_in_group[index] = dist_set

    num_of_group = len(p_set)
    group_data = kmeans.arrangement(dist_in_group, num_of_group)
    print(group_data)

#Test_arrangement()

def Test_means():
    kmeans = Kmeans.kmeans()
    xdata = kmeans.gen_xdata()
    p_set = []
    for i in range(3):
        indx = rnd.randint(0, len(xdata))
        p_set.append(xdata[indx])
    print('p_set', p_set)
    dist_in_group = {}
    for index, p in enumerate(p_set):
        dist_set = kmeans.distance(p)
        dist_in_group[index] = dist_set

    num_of_group = len(p_set)
    group_data = kmeans.arrangement(dist_in_group, num_of_group)
    kmeans.means(group_data)

#Test_means()

def Test_classify_in_kmeans():
    kmeans = Kmeans.kmeans(2, 100)
    kmeans.classify_in_kmeans(4, [67,22])

Test_classify_in_kmeans()