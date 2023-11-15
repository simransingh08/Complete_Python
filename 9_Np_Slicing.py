#Array Slicing

import numpy as np 

# Create a 1D array
arr = np.array([1,2,3,4,5,6,7,98,7,55,4,5]);

#slice array1 from index 3 to 8 (exclusinve)
print (arr[3:8])

#slice array1 from index 0 to 8 (exclusive) with a step 2
print(arr[0:8:2])

#slice array1 from index 3 upto the last element
print(arr[3:])

#items from start to end
print(arr[:])
