import numpy as np 
#creating a array and checking type of the datatype

arr = np.array([1,2,3,4,5]);
print(arr.dtype);

int_arr = np.array([-3,-2,0,1]);
print(int_arr.dtype);

float_arr = np.array([0.1,0.2,0.3]);
print(float_arr.dtype);

complex_arr = np.array([1+2j,2+3j,3+4j]);
print(complex_arr.dtype);
