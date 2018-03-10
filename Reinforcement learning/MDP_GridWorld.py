# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 21:51:54 2018

@author: James
"""
import random as rand

states = [1,2,3,4,5,6,7,8]
actions = ['n','s','w','e']

rewards = dict()
rewards['1_s'] = -1
rewards['3_s'] = 1
rewards['5_s'] = -1
rewards['1_e'] = 0
rewards['2_w'] = 0
rewards['2_e'] = 0
rewards['3_w'] = 0
rewards['3_e'] = 0
rewards['4_w'] = 0
rewards['4_e'] = 0
rewards['5_w'] = 0

trans = dict();             #状态转移的数据格式为字典
trans['1_s'] = 6
trans['1_e'] = 2
trans['2_w'] = 1
trans['2_e'] = 3
trans['3_s'] = 7
trans['3_w'] = 2
trans['3_e'] = 4
trans['4_w'] = 3
trans['4_e'] = 5
trans['5_s'] = 8
trans['5_w'] = 4

terminal_stateas = [6,7,8]
state_value_arr = [0] * len(states)
next_state = init_state
cnt = 0

while cnt<=100:
    temp = 0
    init_state = rand.randint(1,8)
    if init_state in terminal_stateas:
        continue
    for key in trans:
        if str(init_state) in key:
            print(key)
            temp += rewards[key] + state_value_arr[trans[key] - 1]
    
    state_value_arr[init_state - 1] = temp
    print(state_value_arr)
    cnt+=1    
    '''
    action = actions[rand.randint(0,3)]
    stat_act = '_'.join([str(next_state),action])
    print(stat_act)
    pre_state = next_state
    if stat_act in trans:
        next_state = trans[stat_act]
    else:
        cnt+=1
        continue
    
    state_value = rewards[stat_act] + state_value_arr[trans[stat_act]-1]
    state_value_arr[pre_state] = state_value
    
    cnt+=1
    if next_state in terminal_stateas:
        break
    '''
