# Reshape 1D array to 2D array in numpy

import numpy as np

array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])

# reshape a 1D array into a 2D array 
# with 2 rows and 4 columns
result = np.reshape(array1, (2, 4))
print(result)