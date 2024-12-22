import numpy as np
# Task 1 
random_arr=np.random.randint(0,20,12)
print(random_arr)
# reshape the array 3x4 matrix
reshape_arr=random_arr.reshape(3,4)
print(reshape_arr)

# Task 2
arr=np.array([34,56,23,89,12,48,67])

print(f"Maximum value: {arr.max()} at index {arr.argmax()}")
print(f"Minimum value: {arr.min()} at index {arr.argmin()}")