from numpy import random
from flappy_v2 import Flappy

class QLearningAgent:

    def __init__(self, alpha, gamma, it, epsilon):
        self.agent = Flappy()
        self.state = self.agent.get_state()
        self.Q_ = {}
        self.alpha = alpha
        self.gamma = gamma
        self.it = it
        self.t = 0
        self.epsilon = epsilon

    def _reset(self):
        self.agent = Flappy()

    def get_action(self):
        # sample action with epsilon greediness
        if np.random.random() > self.epsilon:
            action = np.argmax(self.Q_.get(self.state, [0, 0]))
        else:
            action = random.randint(2)

    def update(self, s, reward, action):
        dQ = reward + self.gamma * np.max(self.Q_[s]) - self.Q_[self.state]
        self.Q_[self.state] = self.Q_.get(self.state, 0) + self.alpha * dQ
        self.state_ = s
        self.t += 1
