# Using start, stop and step parameter
import numpy as np 
num = np.array([45,56,8,9,3,5,35,6,5,6,55]);

#modify every second element from indices 1 to 5
num[1:3:3] = 16;
print(num);
