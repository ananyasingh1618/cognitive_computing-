import numpy as np
import matplotlib.pyplot as plt
initials_ascii_sum = ord('A') + ord('S')  
X = initials_ascii_sum
sales = np.array([X, X+50, X+100, X+150, X+200])
tax_rate = ((X % 5) + 5) / 100
sales_after_tax = sales * (1 - tax_rate) 
discounted_sales = np.where(sales < X+100, sales * 0.95, sales * 0.90)      
sales_weekly = np.tile(sales, (3, 1)) * np.array([1, 1.02, 1.04]).reshape(3, 1)     
print("Sales after tax:", sales_after_tax)
print("Discounted sales:", discounted_sales)
print("Sales for 3 weeks:", sales_weekly)