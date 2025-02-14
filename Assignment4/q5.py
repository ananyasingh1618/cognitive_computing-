import numpy as np  
ucs420_ananya = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])  
mean_value = np.mean(ucs420_ananya)  
median_value = np.median(ucs420_ananya)  
max_value = np.max(ucs420_ananya)  
min_value = np.min(ucs420_ananya)  
unique_values = np.unique(ucs420_ananya)  
print("Mean  ", mean_value)  
print("Median  ", median_value)  
print("Max  ", max_value)  
print("Min  ", min_value)  
print("Unique Elements  ", unique_values)  
reshaped_ucs420 = ucs420_ananya.reshape(4, 3)  
print("Reshaped Array:", reshaped_ucs420)  
resized_ucs420 = np.resize(ucs420_ananya, (2, 3))  
print("Resized Array:", resized_ucs420)  