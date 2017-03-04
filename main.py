import time
import matplotlib.pyplot as plt

from q_learning import QLearningAgent

learning_agent = QLearningAgent(alpha=0.1, gamma=0.2, it=-1, epsilon=0.3)
max_count_games = 1000
lifetimes = []
count_games = 0

while count_games < max_count_games:
    game_over = False
    while not game_over:
        learning_agent.agent.display_state()
        action = learning_agent.get_action()
        #print('action', action)
        learning_agent.agent.move(action)
        next_state = learning_agent.agent.get_state()
        reward = learning_agent.agent.get_reward()
        learning_agent.update(next_state, reward, action)
        game_over = learning_agent.agent.HIT
        #time.sleep(1)
        print(reward)
    print('GAME OVER')
    lifetimes.append(learning_agent.t)
    learning_agent.reset()
    count_games += 1

print(lifetimes)
