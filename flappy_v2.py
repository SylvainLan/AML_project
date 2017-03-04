import numpy as np
from numpy import random

class Flappy:
    def __init__(self):
        self.y = 0.5
        self.t = 0.
        self.vy = 0.
        self.d_o = 10.
        self.H_o = random.rand()/2. + 0.1
        self.g = 0.1
        self.HIT = False

    def move(self , a):
        if a == 0:
            self.vy -= self.g
        else:
            self.vy = self.g 
#FIXME 
        
        self.y += self.vy
#deltaT 
        self.t += 1
        self.d_o -= 1

        if self.y <= 0:
            self.HIT = True
        if self.d_o <= 0:
            if self.H_o >= self.y or self.H_o + 0.3 <= self.y:
                self.HIT = True

            else:
                self.d_o = random.randint(5,10)
                self.H_o = random.randint(5)/10.

    def get_state(self):
        return [self.y , self.vy , self.d_o , self.H_o]

    def get_reward(self):
        if self.HIT:
            return -1
        else:
            return 1

    def display_state(self):
        print("hauteur :", self.y)
        print("vitesse verticale : " , self.vy)
        print("distance parcourue : ", self.t)
        print("distance au prochain obstacle : " , self.d_o)
        print("hauteur prochain obstacle :" , self.H_o)

