import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
roll_number=102317155
np.random.seed(roll_number)
sales_data = np.random.randint(1000, 5001, size=(12, 4))
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df = pd.DataFrame(sales_data, columns=categories, index=months)
print(df)
print(df.head())
print(df.describe())
df['Total Sales'] = df.sum(axis=1)
category_totals = df[categories].sum()
print(category_totals)
print(df['Total Sales'])
df['Growth Rate'] = df['Total Sales'].pct_change() * 100
discount_category = 'Electronics' if roll_number % 2 == 0 else 'Clothing'
df[discount_category] *= 0.90 if discount_category == 'Electronics' else 0.85
print(df.head())
plt.figure(figsize=(10, 6))
for category in categories:
    plt.plot(months, df[category], label=category)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trends')
plt.show()
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[categories])
plt.title('Sales Distribution')
plt.show()