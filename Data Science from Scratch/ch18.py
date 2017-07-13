# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:54:49 2017

@author: 2017041801
"""
import numpy as np
import math
from matplotlib import pyplot as plt

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_output(weight, x, bias):
    cal = np.dot(weight, x) + bias
    return step_function(cal)

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weight, x):
    return sigmoid(np.dot(weight,x))

def feed_forward(neuron, inputs):
    outputs=[]
    
    for layer in neuron:
        inputs_with_bias = inputs + [1]
        output = [neuron_output(neuron, inputs_with_bias) for neuron in layer]
        outputs.append(output)
    inputs = output
    return outputs    

def back_propagation(inputs, outputs, ini_weight, bias, num_hidden = 2, eta = 0.5):
    #output back to hidden
    w_h = np.ones([(len(inputs) + 1), num_hidden])
    vx = np.zeros(len(inputs) + 1)
    vx[0] = bias[0]
    vx.extend(inputs)
    net_h = np.dot(w_h, vx)
    out_h = sigmoid(net_h)
    
    w_o = np.ones(num_hidden + 1, len(outputs))
    net_y = np.dot(w_o, [bias[1], out_h])
    out_y = sigmoid(net_y)
    
    p1 = -(np.array(outputs) - np.array(out_y))
    p2 = np.array(out_y) * (np.ones(len(out_y)) - np.array(out_y))
    p3 = np.array(out_h)
    delta_rule = p1 * p2 * p3
                  
    new_w_h = w_h - eta * delta_rule
    
    return new_w_h
    #hidden back to input
    
    
#w = back_propagation([0.05, 0.1], [0.1, 0.99], np.ones(8), [0.35,0.6])

vx=[0,0]
vx[0] = 1   
print(vx[0])    
    
    
    
    