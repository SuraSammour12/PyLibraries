import numpy as np
# Task 1: Create a 1D Numpy array from a list
my_list=[5,10,15,20,25]
np_array=np.array(my_list)
print(f"1D Array : {np_array}")
print(f"Type : {type(np_array)}")
print('------------------------------------------------------------------')
# Task 2: Create a 3x2 NumPy array:
matrix=[[10,20],[30,40],[50,60]]
np_array2=np.array(matrix)
print(f"2D Array (3x2) : {np_array2}")
print(f"Type : {type(np_array2)}")
print('------------------------------------------------------------------')
# Task 3: Create a 3x5 NumPy array:
lst=[[1,2,3,4,5],[5,7,8,9,10],[11,12,13,14,15]]
np_array3=np.array(lst)
print(f"2D Array (3x5) : {np_array3}")
print(f"Type : {type(np_array3)}")