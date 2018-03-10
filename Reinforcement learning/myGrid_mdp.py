# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 21:24:35 2018

@author: James
"""

import logging
import numpy
import random
from gym import spaces
import gym

logger = logging.getLogger(__name__)

class GridEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):

        self.states = [s for s in range(1,19)] #状态空间
        self.x=[140,220,300,460,140,220,300,460,300,380,460,140,220,300,380,460,140,220]
        self.y=[450,450,450,450,350,350,350,350,250,250,250,150,150,150,150,150,50,50]
        self.terminate_states = dict()  #终止状态为字典格式
        self.terminate_states[11] = 1

        self.actions = ['n','e','s','w']

        self.rewards = dict();        #回报的数据结构为字典
        self.rewards['8_s'] = 1.0
        self.rewards['10_e'] = 1.0
        self.rewards['16_n'] = 1.0

        self.t = dict();             #状态转移的数据格式为字典
        self.t['1_s'] = 5
        self.t['1_e'] = 2
        self.t['2_w'] = 1
        self.t['2_e'] = 3
        self.t['2_s'] = 6
        self.t['3_s'] = 7
        self.t['3_w'] = 2
        self.t['4_s'] = 8
        self.t['5_n'] = 1
        self.t['5_e'] = 6
        self.t['6_w'] = 5
        self.t['6_n'] = 2
        self.t['6_e'] = 7
        self.t['7_n'] = 3
        self.t['7_s'] = 9
        self.t['7_w'] = 6
        self.t['8_n'] = 4
        self.t['8_s'] = 11
        self.t['9_n'] = 7
        self.t['9_w'] = 10
        self.t['9_s'] = 14
        self.t['10_w'] = 9
        self.t['10_s'] = 15
        self.t['10_e'] = 11
        self.t['12_e'] = 13
        self.t['12_s'] = 17
        self.t['13_e'] = 14
        self.t['13_n'] = 18
        self.t['14_n'] = 9
        self.t['14_e'] = 15
        self.t['14_w'] = 13
        self.t['15_n'] = 10
        self.t['15_e'] = 16
        self.t['15_w'] = 14
        self.t['16_n'] = 11
        self.t['16_w'] = 15
        self.t['17_n'] = 12
        self.t['17_e'] = 18
        self.t['18_n'] = 13
        self.t['18_w'] = 17

        self.gamma = 0.8         #折扣因子
        self.viewer = None
        self.state = None

    def getTerminal(self):
        return self.terminate_states

    def getGamma(self):
        return self.gamma

    def getStates(self):
        return self.states

    def getAction(self):
        return self.actions
    def getTerminate_states(self):
        return self.terminate_states
    def setAction(self,s):
        self.state=s

    def _step(self, action):
        #系统当前状态
        state = self.state
        if state in self.terminate_states:
            return state, 0, True, {}
        key = "%d_%s"%(state, action)   #将状态和动作组成字典的键值

        #状态转移
        if key in self.t:
            next_state = self.t[key]
        else:
            next_state = state
        self.state = next_state

        is_terminal = False

        if next_state in self.terminate_states:
            is_terminal = True

        if key not in self.rewards:
            r = 0.0
        else:
            r = self.rewards[key]


        return next_state, r,is_terminal,{}
    def _reset(self):
        self.state = self.states[int(random.random() * len(self.states))]
        return self.state
    def render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return
        screen_width = 600
        screen_height = 600

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)
            #创建网格世界
            self.line1 = rendering.Line((100,500),(340,500))
            self.line2 = rendering.Line((100,400),(340,400))
            self.line3 = rendering.Line((100,300),(340,300))
            self.line4 = rendering.Line((100,500),(100,300))
            self.line5 = rendering.Line((180,500),(180,300))
            self.line6 = rendering.Line((260,500),(260,300))
            self.line7 = rendering.Line((340,500),(340,300))
            
            self.line8 = rendering.Line((420,500),(500,500))
            self.line9 = rendering.Line((420,400),(500,400))
            self.line10 = rendering.Line((420,300),(500,300))
            self.line11 = rendering.Line((420,500),(420,300))
            self.line12 = rendering.Line((500,500),(500,300))

            self.line13 = rendering.Line((260, 300), (500, 300))
            self.line14 = rendering.Line((260, 200), (500, 200))
            self.line15 = rendering.Line((260, 100), (500, 100))
            self.line16 = rendering.Line((260, 300), (260, 100))
            self.line17 = rendering.Line((340, 300), (340, 100))
            self.line18 = rendering.Line((420, 300), (420, 100))
            self.line19 = rendering.Line((500, 300), (500, 100))
            
            self.line20 = rendering.Line((100, 200), (260, 200))
            self.line21 = rendering.Line((100, 100), (260, 100))
            self.line22 = rendering.Line((100, 0), (260, 0))
            self.line23 = rendering.Line((100, 200), (100, 0))
            self.line24 = rendering.Line((180, 200), (180, 0))
            self.line25 = rendering.Line((260, 200), (260, 0))     
            
            #创建金条
            self.gold = rendering.make_circle(40)
            self.circletrans = rendering.Transform(translation=(460, 250))
            self.gold.add_attr(self.circletrans)
            self.gold.set_color(1, 0.9, 0)
            #创建机器人
            self.robot= rendering.make_circle(30)
            self.robotrans = rendering.Transform()
            self.robot.add_attr(self.robotrans)
            self.robot.set_color(0.8, 0.6, 0.4)

            self.line1.set_color(0, 0, 0)
            self.line2.set_color(0, 0, 0)
            self.line3.set_color(0, 0, 0)
            self.line4.set_color(0, 0, 0)
            self.line5.set_color(0, 0, 0)
            self.line6.set_color(0, 0, 0)
            self.line7.set_color(0, 0, 0)
            self.line8.set_color(0, 0, 0)
            self.line9.set_color(0, 0, 0)
            self.line10.set_color(0, 0, 0)
            self.line11.set_color(0, 0, 0)
            self.line12.set_color(0, 0, 0)
            self.line13.set_color(0, 0, 0)
            self.line14.set_color(0, 0, 0)
            self.line15.set_color(0, 0, 0)
            self.line16.set_color(0, 0, 0)
            self.line17.set_color(0, 0, 0)
            self.line18.set_color(0, 0, 0)
            self.line19.set_color(0, 0, 0)
            self.line20.set_color(0, 0, 0)
            self.line21.set_color(0, 0, 0)
            self.line22.set_color(0, 0, 0)
            self.line23.set_color(0, 0, 0)
            self.line24.set_color(0, 0, 0)
            self.line25.set_color(0, 0, 0)

            self.viewer.add_geom(self.line1)
            self.viewer.add_geom(self.line2)
            self.viewer.add_geom(self.line3)
            self.viewer.add_geom(self.line4)
            self.viewer.add_geom(self.line5)
            self.viewer.add_geom(self.line6)
            self.viewer.add_geom(self.line7)
            self.viewer.add_geom(self.line8)
            self.viewer.add_geom(self.line9)
            self.viewer.add_geom(self.line10)
            self.viewer.add_geom(self.line11)
            self.viewer.add_geom(self.line12)
            self.viewer.add_geom(self.line13)
            self.viewer.add_geom(self.line14)
            self.viewer.add_geom(self.line15)
            self.viewer.add_geom(self.line16)
            self.viewer.add_geom(self.line17)
            self.viewer.add_geom(self.line18)
            self.viewer.add_geom(self.line19)
            self.viewer.add_geom(self.line20)
            self.viewer.add_geom(self.line21)
            self.viewer.add_geom(self.line22)
            self.viewer.add_geom(self.line23)
            self.viewer.add_geom(self.line24)
            self.viewer.add_geom(self.line25)
            self.viewer.add_geom(self.gold)
            self.viewer.add_geom(self.robot)

        if self.state is None: return None
        #self.robotrans.set_translation(self.x[self.state-1],self.y[self.state-1])
        self.robotrans.set_translation(self.x[self.state-1], self.y[self.state- 1])



        return self.viewer.render(return_rgb_array=mode == 'rgb_array')