# Using start parameter
import numpy as np 
#create a numpy 1D array
num = np.array([9,8,7,6,5,4,32,12,45]);

#modify elements from index 3 onwards
num[3:] = 55;
print(num)