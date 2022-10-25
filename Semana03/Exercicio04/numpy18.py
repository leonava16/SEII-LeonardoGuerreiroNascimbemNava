import numpy as np

# np.loadtxt, np.genfromtxt
data = np.genfromtxt('spambase.csv', delimiter=",", dtype=np.float32)
print(data.shape)