from q_learning import QLearningAgent

agent = QLearningAgent()
max_count_games = 10
count_games = 0

while count_games < max_count_games:
    game_over = False
    while not game_over
        self.agent.display_state()
        action = self.get_action()
        self.agent.move(action)
        next_state = self.agent.get_state()
        reward = self.agent.get_reward()
        self.update(next_state, reward, action)
        game_over = ~self.agent.HIT
    print('GAME OVER')
    count_games += 1
