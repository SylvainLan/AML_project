
from flappy_v2 import Flappy

flappy = Flappy()

while not flappy.HIT:
    action = int(raw_input())
    flappy.move(action)
    flappy.display_state() 
