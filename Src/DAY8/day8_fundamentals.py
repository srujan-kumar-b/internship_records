import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)

arr = np.random.rand(10)
squared = arr ** 2
print(arr)

zeroes_array = np.zeros((3, 4))
print("Zeroes array:\n", zeroes_array)
one_d_array = np.array([1, 2, 3, 4, 5])
print("One-dimensional array:\n", one_d_array)        
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Two-dimensional array:\n", two_d_array)      
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Three-dimensional array:\n", three_d_array)

print("Reshaped array:")
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

# Reshaping to a different shape
print("vstack:")
a = np.array([[1, 2]])
b = np.array([[3, 4]])
vstacked = np.vstack((a, b))
print(vstacked)

print("hstack:")
hstacked = np.hstack((a, b))
print(hstacked)

#mean#
data = np.array([[10, 20, 30],
                 [40, 50, 60]])
print(np.mean(data))  
print(np.mean(data, axis=0)) 
print(np.mean(data, axis=1)) 


A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print(np.dot(A, B))