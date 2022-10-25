import numpy as np

a = np.array([[1,2], [3,4]])
print(a)
print(a.shape)

c = np.diag(a)
print(np.diag(c))