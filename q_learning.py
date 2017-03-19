import numpy as np

from numpy import random
from flappy import Flappy

class QLearningAgent:

    def __init__(self, alpha, gamma, it, epsilon):
        self.agent = Flappy()
        self.state = tuple(self.agent.get_state())
        self.Q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.t = 0
        self.warm_start = -1
        self.epsilon = epsilon


    def reset(self):
        self.agent = Flappy()
        self.t = 0


    def get_action(self):
        if self.t < self.warm_start:
            action = random.randint(2)
        else:
            # sample action with epsilon greediness
            if np.random.random() > self.epsilon:
                self.Q[self.state] = self.Q.get(self.state, [0, 0])
                action = np.argmax(self.Q[self.state])
            else:
                action = random.randint(2)
        return action


    def update(self, s, reward, action):
        s = tuple(s)
        self.Q[self.state] = self.Q.get(self.state, [0, 0])
        self.Q[s] = self.Q.get(s, [0, 0])
        dQ = reward + self.gamma * np.max(self.Q[s]) - self.Q[self.state][action]
        self.Q[self.state][action] += self.alpha * dQ
        self.state = s
        self.t += 1
