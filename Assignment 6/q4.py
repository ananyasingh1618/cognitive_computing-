import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv")
plt.plot(df['month_number'], df['total_profit'])
plt.title('Total Profit Over Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid()
plt.show()
df.plot(x='month_number', y=df.columns[1:], kind='line')
plt.title('Product Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid()
plt.show()
df.plot(kind='bar', figsize=(10, 6))
plt.title('All Features Data')
plt.grid()
plt.show()