
from flappy import Flappy

flappy = Flappy()

while not flappy.HIT:
    action = int(input())
    flappy.move(action)
    flappy.display_state()
