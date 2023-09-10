import numpy as np

y = np.array([1, -1, -1, -1, -1])
y1 = np.argmax(np.tile(y, (1000, 1)), axis=1)

print(y1)
