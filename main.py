from numpy import random

import time
import matplotlib.pyplot as plt

from q_learning import QLearningAgent

learning_agent = QLearningAgent(alpha=0.1, gamma=0.9, it=-1, epsilon=0.1)
learning_agent.agent.display_mode = False
max_count_games = 100
lifetimes = []
count_games = 0
random_games = 10

while count_games < max_count_games:
    game_over = False
    reward = 0
    while not game_over:
        if count_games < random_games:
            action = random.randint(2)
        else:
            action = learning_agent.get_action()
        #print('action', action)
        learning_agent.agent.move(action)
        next_state = learning_agent.agent.get_state()
        #learning_agent.agent.display_state()
        reward += learning_agent.agent.get_reward()
        learning_agent.update(next_state, reward, action)
        game_over = learning_agent.agent.HIT
        #time.sleep(1)
        #print(reward)
    #print('GAME OVER')
    lifetimes.append(learning_agent.t)
    learning_agent.reset()
    count_games += 1

print(lifetimes)
print(max(lifetimes))
