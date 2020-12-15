import numpy as np
import time


a = np.matrix([
    [1, 2, 3],
    [4, 5, 6],
])

start_time = time.time()

for i in range(1000):
    check = 6 not in a

print("--- %s seconds ---" % (time.time() - start_time))

# 0.03390884399 (np.any(a == 6))