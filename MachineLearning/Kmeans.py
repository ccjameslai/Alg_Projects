import numpy as np
import random as rnd
import math
from matplotlib import pyplot as plt


class kmeans(object):
    def __init__(self, dim, size):
        x = []
        for i in range(dim*size):
            x.append(rnd.randint(0, 100))
        temp = []
        self.xdata = []
        cnt = 0
        for sx in x:
            temp.append(sx)
            cnt += 1
            if cnt%dim == 0:
                xtemp = temp[:]
                self.xdata.append(xtemp)
                cnt = 0
                temp = []

    def gen_xdata(self):
        return self.xdata

    def distance(self, point):
        dist_set = []
        for x in self.xdata:
            diff = np.array(x)-np.array(point)
            diff_sqr = diff.dot(diff)
            d = math.sqrt(diff_sqr)
            dist_set.append(d)
        return dist_set

    def arrangement(self, dist_in_group, num_of_group):
        group = {}
        for g in range(num_of_group):
            group[g] = []

        data_list = []
        for _, d in dist_in_group.items():
            data_list.append(d)

        for i in range(len(data_list[0])):
            temp = []
            for j in range(num_of_group):
                temp.append(data_list[j][i])
            index = temp.index(min(temp))
            group[index].append(self.xdata[i])

        return group

    def means(self, group):
        means = []
        for g, d in group.items():
            d_sum = sum(np.array(d))
            means.append(d_sum / len(d))

        return means

    def classify_in_kmeans(self, k, query):
        p_set = []
        for i in range(k):
            indx = rnd.randint(0, len(self.xdata))
            p_set.append(self.xdata[indx])

        diff = 10000
        while abs(diff) > 0.000001:
            dist_in_group = {}
            for index, p in enumerate(p_set):
                dist_set = kmeans.distance(self, p)
                dist_in_group[index] = dist_set

            num_of_group = len(p_set)
            group_data = kmeans.arrangement(self, dist_in_group, num_of_group)
            new_means = kmeans.means(self, group_data)

            diff = sum(sum(np.array(p_set))) - sum(sum(new_means))
            p_set = new_means

        dist_set = []
        for i in range(len(p_set)):
            diff = np.array(p_set[i]) - np.array(query)
            diff_sqr = diff.dot(diff)
            d = math.sqrt(diff_sqr)
            dist_set.append(d)

        group = (dist_set.index(min(dist_set)) + 1)
        print('group and cord', group, p_set[group - 1])

        x_set = [x[0] for x in self.xdata]
        y_set = [x[1] for x in self.xdata]
        plt.scatter(x_set, y_set, c='b', marker='o')
        for p in p_set:
            plt.scatter(p[0], p[1], c='r', marker='*')
        plt.scatter(query[0], query[1], c='g', marker='*')
        plt.show()



