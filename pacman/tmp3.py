import hashlib
import numpy as np


a = np.matrix([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.matrix([
    [1, 2, 3],
    [4, 5, 7]
])
# one more time -> different hash code
hvalue = hashlib.sha1(b.tobytes()).hexdigest()
print(type(hvalue))  # --> e12b2fe9d64df2661920eb81afb4d3bbd416e0bb

hvalue = hashlib.sha1(a.tobytes()).hexdigest()
print(hvalue)  #