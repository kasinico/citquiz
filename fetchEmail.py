# Create NumPy arrays
import numpy as np

arr = np.array([[3, 5, 7, 9, 11],
               [2, 4, 6, 8, 10]])
               

# Use slicing a 2-D arrays
arr2 = arr[1:,1:3]
print(arr2)  

# Output
#[[4 6]]

# import numpy module
import numpy as np

# Create NumPy arrays
arr = np.array([[3, 5, 7, 9, 11],
               [2, 4, 6, 8, 10]])

# Use slicing to get 1-D arrays elements
arr2 = arr[1:6]
print(arr2) 

# OutPut
# [ 5  7  9 11 15]