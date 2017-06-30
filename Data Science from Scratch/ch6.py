# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:48:23 2017

@author: 2017041801
"""
import random as rnd
import math
from matplotlib import pyplot as plt
from collections import Counter

def rnd_kid():
    return rnd.choice(['boy', 'girl'])

def normal_pdf(x, mu=0, sigma=1):
    sqrt_2_pi = math.sqrt(2 * math.pi)
    return math.exp(-(x-mu)**2/2/sigma**2) / (sqrt_2_pi * sigma)

def normal_cdf(x, mu=-2,sigma=1):
    return (1 + math.erf((x-mu)/math.sqrt(2)/sigma)) / 2

def inverse_normal_cdf(p, mu=-2, sigma=1, tolerance=0.00001):
    lo, hi = -10,10
    while hi - lo > tolerance:
        mid = (lo + hi) / 2
        midp = normal_cdf(mid)
        if midp > p:
            hi = mid
        elif midp < p:
            lo = mid
        else:
            break
    return mid

def bernoulli_trail(p):
    return 1 if rnd.random() > p else 0

def binomial(n, p):
    xs = [x for x in range(n)]
    ys = [bernoulli_trail(p) for _ in range(n)]
    plt.plot(xs, ys, 'o')
    return sum(bernoulli_trail(p) for _ in range(n))

def make_hist(n, p, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    histogram = Counter(data)
    xs = [k - 0.4 for k, _ in histogram.items()]
    ys = [v / num_points for _, v in histogram.items()]
    plt.bar(xs, ys, 0.8)
    
    m = n * p
    sig = math.sqrt(n * p * (1 - p))
    xss = range(100)
    normal_ys = [normal_pdf(x, m, sig) for x in xss]
    #normal_ys = [normal_cdf(x + 0.5, m, sig) - normal_cdf(x - 0.5, m, sig) for x in xss]
    plt.plot(xss, normal_ys, 'r')
    plt.axis([0,100,0,0.1])
    plt.show()
#xs = [x / 10 for x in range(-50,50)]
#plt.plot(xs, [normal_cdf(x) for x in xs])

#print(normal_cdf(2))
#print(inverse_normal_cdf(0.9772498680518207))
#make_hist(100, 0.3, 1000)
#print(normal_pdf(30, 70, math.sqrt(21)))
#print(binomial(100, 0.3))
#print(Counter([binomial(100, 0.3) for _ in range(10)]))
binomial(100, 0.3)