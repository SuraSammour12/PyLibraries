# Creating NumPy Arrays : From a Python List
import numpy as np
my_list=[1,2,3,4,5,6]
print(type(my_list))

np_list=np.array(my_list)
print(type(np_list))

my_matrix=[[1,2,3],[4,5,6]]
np_matrix=np.array(my_matrix)
print(my_matrix)
print(type(np_matrix))