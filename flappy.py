import numpy as np

class Environment:
    def __init__(self, agent, args = None):
        self.state = np.zeros(5)
#Height ofn the bird, vertical speed of the bird, distance to next obstacle,
#height of the obstacle, width of the obstacle
        self.state[0] = 0.5
#The height is between 0 and 1
        self.state[2] = np.inf
        self.distance = 0.
#The distance that the bird flew, criterion to maximize
        self.theta = self.state[0] 
#Angle of the speed, considering the longitudinal speed is 1
        self.time = 0.

        self.v_i = 1
        self.y_1 = 0.5
        
        g = 10
#Gravitational constant
        
        self.HIT = False

    def moveBird(self , a):
        if a == 0:
            self.distance += 0.1 * theta
            self.state[0] = -1/2*g*self.time^2 + self.y_i
            self.state[1] = self.time * g
            self.state[2] -= self.distance

            if self.state[0] <= 0:
                self.HIT = True
            if self.state[2] <= 0 and self.state[0] <= self.state[3]:
                self.HIT = True
            if self.state[2] <= 0 and self.state[0] >= self.state[4]:
                self.HIT = True

            if self.state[2] <= 0:
                if np.random.uniform() < epsilon:
                    self.state[2] = self.random.uniform(0.5,1.)
                    self.state[3] = np.random.uniform()
                    self.state[4] = np.random.uniform(self.state[3] , 1)
                else:
                    self.state[2] = np.inf


