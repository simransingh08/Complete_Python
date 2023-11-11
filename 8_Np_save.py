import numpy as np

# create a NumPy array
array1 = np.array([[1, 3, 5],[7, 9, 11]])

# save the array to a file
np.save('file1.npy', array1)