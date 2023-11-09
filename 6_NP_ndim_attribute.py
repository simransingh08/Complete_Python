#ndim attribute check the dimension of the array

import numpy as np 
arr = np.array([1,2,3]);
print(arr.ndim);

arr1 = np.array([[1,2,3],[4,5,6]]);
print(arr1.ndim);

arr2 = np.array([[11,22,33],[111,222,333],[1111,2222,3333]]);
print(arr2.ndim);