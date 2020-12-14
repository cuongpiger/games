import numpy as np
from modules.boards import boards



a = np.matrix([
    [1, 2, 3],
    [4, 5, 6]
])

r, c = a.shape

print(r, c)