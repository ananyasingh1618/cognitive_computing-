import numpy as np  
x = np.array([1,2,3,4,5,1,2,1,1,1])  
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])  
mostfrequent_x = np.bincount(x).argmax()  
mostfrequent_y = np.bincount(y).argmax()  
indices_x = np.where(x == mostfrequent_x)[0]  
indices_y = np.where(y == mostfrequent_y)[0]  
print("Most Frequent value in x:", mostfrequent_x, "Indices:", indices_x)  
print("Most Frequent value  in y:", mostfrequent_y, "Indices:", indices_y)  