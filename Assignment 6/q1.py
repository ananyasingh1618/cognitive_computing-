import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
M = float(input())
x = np.linspace(-10, 10, 400)
df = pd.DataFrame({'x': x, 'y1': M * x**2, 'y2': M * np.sin(x)})
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x='x', y='y1', color="r", linestyle="-", label="y = Mx²")
sns.lineplot(data=df, x='x', y='y2', color="b", linestyle="--", label="y = Msin(x)")
plt.legend()
plt.title('Mathematical Functions')
plt.show()
