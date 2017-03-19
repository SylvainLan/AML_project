import numpy as np

from numpy import random
from flappy import Flappy

class QLearningAgent:

    def __init__(self, alpha, gamma, it, epsilon):
        self.agent = Flappy()
        self.state = tuple(self.agent.get_state())
        self.Q_ = {}
        self.alpha = alpha
        self.gamma = gamma
        self.it = it
        self.t = 0
        self.epsilon = epsilon


    def reset(self):
        self.agent = Flappy()
        self.t = 0
        

    def get_action(self):
        # sample action with epsilon greediness
        if np.random.random() > self.epsilon:
            action = np.argmax(self.Q_.get(self.state, [0, 0]))
#FIXME rand for the case we were not in the state before ? 
        else:
            action = random.randint(2)
        return action


    def update(self, s, reward, action):
        s = tuple(s)
        dQ = reward + self.gamma * np.max(self.Q_.get(s,0)) - self.Q_.get(self.state,0)
        self.Q_[self.state] = self.Q_.get(self.state, 0) + self.alpha * dQ
        self.state_ = s
        self.t += 1
