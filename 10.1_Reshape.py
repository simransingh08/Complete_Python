import numpy as np

# reshape a 1D array into a 2D array 
# with 4 rows and 2 columns
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
result1 = np.reshape(array1, (4, 2))
print("With 4 rows and 2 columns: \n",result1)


# reshape a 1D array into a 2D array with a single row
result2 = np.reshape(array1, (1, 8))
print("\nWith a single row: \n",result2)