import numpy as np
import matplotlib.pyplot as plt
array = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_array = np.sort(array)  
sorted_indices = np.argsort(array)  
smallest_4 = np.sort(array)[:4] 
largest_5 = np.sort(array)[-5:] 
print("Sorted array:", sorted_array)
print("Indices of sorted array:", sorted_indices)
print("4 smallest elements:", smallest_4)
print("5 largest elements:", largest_5)
floats = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integer_elements =floats[floats == floats.astype(int)]
float_elements = floats[floats != floats.astype(int)]
print("Integer elements:", integer_elements)
print("Float elements:", float_elements)