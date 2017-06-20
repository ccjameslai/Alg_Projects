# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:46:11 2017

@author: 2017041801
"""

def Newton_method(d_func, d2_func, ini_value, e = pow(10, -5)):
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