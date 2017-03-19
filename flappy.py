import numpy as np
from numpy import random

class Flappy:
    def __init__(self, rewards):
        self.y = 0.5
        self.t = 0
        self.vy = 0.
        self.d_o = np.inf
        self.H_o = random.randint(5)/10.
        self.g = 0.1
        self.HIT = False
        self.rewards = rewards

    def move(self , a):
        if a == 0:
            self.vy -= self.g
        else:
            self.vy = self.g

        self.y += self.vy
#deltaT
        self.t += 1
        self.d_o -= 1

        if 0 > self.y or 1 < self.y:
            self.HIT = True
        if self.d_o <= 0:
            if self.H_o >= self.y or self.H_o + 0.3 <= self.y:
                self.HIT = True

            else:
                self.d_o = random.randint(5,10)
                self.H_o = random.randint(5)/10.

    def get_state(self):
        #return [self.y , self.vy , self.d_o , self.H_o]
        return [self.y , self.vy]

    def get_reward(self):
        if self.HIT:
            return self.rewards['hit']
        else:
            return self.rewards['go']

    def display_state(self):
        print("height :", self.y)
        print("vertical speed : " , self.vy)
        print("distance since launch : ", self.t)
        print("distance to next obstacle : " , self.d_o)
        print("height next obstacle :" , self.H_o)
