from gym import Env
from gym.spaces import Discrete
from numpy import random
import numpy as np
from gym.utils import seeding

class randomMaze(Env):

    def __init__(self):
        # action can be taken-> left, right
        self.action_space = Discrete(4)
        # S+ states
        self.observation_space = np.arange(12).reshape(3,4)
        # start state
        self.state = 8
        # episode length
        self.ep_len = 0
        #terminal state
        self.goal = 3
        self.hole = 7
        #wall
        self.wall = 5

    def step(self, action, ini_state):
        env_action = action
        state = ini_state
        # print(state)
        choose = random.random()
        #for 80% time move in the intended dir
        if choose < 0.8:
            if action == 0:
                if state[0]>0 and self.observation_space[state[0]-1][state[1]] != self.wall: 
                    state[0] -= 1
            elif action == 1:
                if state[1]<3 and self.observation_space[state[0]][state[1]+1] != self.wall: 
                    state[1] += 1
            elif action == 2:
                if state[0]<2 and self.observation_space[state[0]+1][state[1]] != self.wall: 
                    state[0] += 1
            elif action == 3:
                if state[1]>0 and self.observation_space[state[0]][state[1]-1] != self.wall: 
                    state[1] -= 1
            
            if state[0]>=0 and state[0]<3 and state[1]>=0 and state[1] < 4 and self.observation_space[state[0]][state[1]] != self.wall:
                self.state = self.observation_space[state[0]][state[1]]
            else:
                state = ini_state
            
            # print(state)
            
            
        #else move left in the 10% cases
        elif choose <0.9:
            env_action = action-1
            if env_action<0:
                env_action = 3
            if action == 0:
                if state[1]>0 and self.observation_space[state[0]][state[1]-1] != self.wall: 
                    state[1] -= 1
            elif action == 1:
                if state[0]>0 and self.observation_space[state[0]-1][state[1]] != self.wall: 
                    state[0] -= 1
            elif action == 2:
                if state[1]<3 and self.observation_space[state[0]][state[1]+1] != self.wall: 
                    state[1] += 1
            elif action == 3:
                if state[0]<2 and self.observation_space[state[0]+1][state[1]] != self.wall: 
                    state[0] += 1
            
            if state[0]>=0 and state[0]<3 and state[1]>=0 and state[1] < 4 and self.observation_space[state[0]][state[1]] != self.wall:
                self.state = self.observation_space[state[0]][state[1]]
            else:
                state = ini_state
                
            # print(state)
                
        # move right otherwise
        else:
            env_action = action+1
            if env_action>3:
                env_action = 0
            if action == 0:
                if state[1]<3 and self.observation_space[state[0]][state[1]+1] != self.wall: 
                    state[1] += 1
            elif action == 1:
                if state[0]<2 and self.observation_space[state[0]+1][state[1]] != self.wall: 
                    state[0] += 1
            elif action == 2:
                if state[1]>0 and self.observation_space[state[0]][state[1]-1] != self.wall: 
                    state[1] -= 1
            elif action == 3:
                if state[0]>0 and self.observation_space[state[0]-1][state[1]] != self.wall: 
                    state[0] -= 1
            
            if state[0]>=0 and state[0]<3 and state[1]>=0 and state[1] < 4 and self.observation_space[state[0]][state[1]] != self.wall:
                self.state = self.observation_space[state[0]][state[1]]
            else:
                state = ini_state
                
            # print(state)
            
                
        if self.state == self.goal:
            reward = 1
        elif self.state == self.hole:
            reward = -1
        else:
            reward = -0.04
            
        self.ep_len +=1
        return self.state,reward,state,env_action

    def render(self):
        pass
    
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np.random(seed)
        return [seed]
    
    def reset(self):
        self.state = 8
        self.ep_len = 0
        return self.state

