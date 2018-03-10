# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:54:44 2018

@author: James
"""

import gym
import random as rnd

env = gym.make('GridWorld-v0')
actions = ['n','w','e','s']
for _ in range(1):
    state = env.reset()
    print('initial state: ', state)
    is_terminal = False
    while not is_terminal:
        env.render()
        action = actions[rnd.randint(0,3)]
        print('action: ', action)
        next_state, r , is_terminal,info = env.step(action)
        print(next_state,r, is_terminal)
    env.render()