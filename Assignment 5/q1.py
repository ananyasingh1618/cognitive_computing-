import numpy as np
import matplotlib.pyplot as plt
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
sum = np.sum(gfg)  
row_sum = np.sum(gfg, axis=1) 
col_sum = np.sum(gfg, axis=0) 
print("Sum of all elements:", sum)
print("Row-wise sum:", row_sum)
print("Column-wise sum:", col_sum)