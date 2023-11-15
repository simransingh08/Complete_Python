import numpy as np

# create a 1D array
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])

# reshape the 1D array to a 3D array
result = np.reshape(array1, (2, 2, 2))

# print the new array
print("1D to 3D Array: \n",result)