import numpy as np 
from pygame.math import Vector2 as vec
from maze import mazes

tmp = mazes[0]
ma = np.array(tmp)



ids = np.where(ma == 0)

walls = [vec(i, j) for i, j in zip(ids[0], ids[1])]

print(walls)