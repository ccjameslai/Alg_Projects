# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:43:12 2017

@author: 2017041801
"""

import numpy as np


def statevalue_with_BellmanEqu(transition_matrix, immediate_reward, gamma):
    pinv_of_transition_matrix = np.linalg.pinv(np.eye(len(transition_matrix)) - gamma*transition_matrix)
        
    return np.dot(pinv_of_transition_matrix, immediate_reward)
         
t_matrix = np.array([(0.9,0.1,0,0,0,0),
                              (0.5,0,0.5,0,0,0),
                              (0,0,0,0.8,0,0),
                              (0,0,0,0,0.4,0.6),
                              (0,0.2,0.4,0.4,0,0),
                              (0,0,0,0,0,0)])
        
reward = np.array((-1,-2,-2,-2,1,10))
gamma = 0.9

print(statevalue_with_BellmanEqu(t_matrix, reward, gamma))
