# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:59:56 2017

@author: 2017041801
"""

import matplotlib.pyplot as plt

def sum_of_square(v):
    return sum(v_i**2 for v_i in v)

def difference_quotient(f,x,h=0.00001):
    return (f(x + h) - f(x)) / h

def extrem_point(f, ini_v, step = -0.1, e = pow(10, -7)):
    iter_num = 0
    while abs(difference_quotient(f, ini_v)) > e:
        gradien = difference_quotient(f, ini_v)
        ini_v += step * gradien
        iter_num = iter_num + 1
        if iter_num == 100000:
            return float('inf'), iter_num
    return ini_v, iter_num

def func(x):
    return 2*(x - 3)**2 + 7

def d_f(x):
    return 4*(x - 3)

def gradien_descent(f, ini_v, step = -0.1, e = pow(10, -7)):
    iter_num = 0
    next_v = 100000
    temp = ini_v
    while abs(next_v - temp) > e:
        gradien = difference_quotient(f, ini_v)
        next_v = ini_v + step * gradien
        temp = ini_v
        ini_v = next_v
        iter_num = iter_num + 1
        if iter_num == 100000:
            return float('inf'), iter_num
    return next_v, iter_num 


v=[2,5,9,4,3,7,8]

f=func
xs = [x for x in range(-10,10)]
ys = [func(i) for i in xs]
min_p, iter_num = extrem_point(f,-5)
gdmin_p, gditer_num = gradien_descent(f,4)
print(min_p, iter_num,gdmin_p, gditer_num)
plt.plot(xs,ys, min_p, f(min_p), 'r^', gdmin_p, f(gdmin_p), 'g*')