import numpy as np

class Flappy:
    def __init__(self):
        self.y = 0.5
        self.t = 0.
        self.vy = 0.
        self.d_o = np.inf
        self.H_o = 0.
        self.L_o = 0.
        self.g = 10.
        self.HIT = False

    def move(self , a):
        if a == 0:
            self.vy -= self.g
        else:
            self.vy = self.g 
#FIXME 
        
        self.y -= self.vy
#deltaT 
        self.t += 1
        self.d_o -= 1

        if self.y <= 0:
            self.HIT = True
        if self.d_o <= 0:
            if self.H_o >= self.y or self.H_o + self. L_o <= self.y:
                self.HIT = True

    def display_state(self):
        print("hauteur :", self.y)
        print("distance parcourue : ", self.t)
        print("distance au prochain obstacle : " , self.d_o)
