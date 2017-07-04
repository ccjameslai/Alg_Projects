# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:46:11 2017

@author: 2017041801
"""



def Newton_method(d_func, d2_func, ini_value, e = pow(10, -5)):
    x = 0
    while abs(d_func(ini_value)) > e:
        x = ini_value - (d_func(ini_value)/d2_func(ini_value))
        ini_value = x
    return x

def golden_search(func, lower, upper, alpha = 0.382, e = pow(10, -6)):
  
    extrem = alpha * (upper - lower) + lower
    while upper - lower > e:
        d = upper - alpha * (upper - lower)
        if func(d) > func(extrem):
            upper = d
        else:
            lower = extrem
            extrem = d
   
        return extrem

def gradien_descent(gfunc, ini_value, lambd, e = pow(10, -5)):
    x = 0
    while abs(gfunc(ini_value)) > e:
        x = ini_value - lambd * gfunc(ini_value)
        ini_value = x
    return x



def max_func_value_and_x(ini_x, func):
    value = 0
    for i in ini_x:
        if value < func(i):
            value = func(i)
            m_x = i
    return [value, m_x]

def min_func_value_and_x(ini_x, func):
    value = 1000000
    for i in ini_x:
        if value > func(i):
            value = func(i)
            m_x = i
    return [value, m_x]    