import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {'Subjects': ['Math', 'Physics', 'Chemistry', 'Biology', 'English'], 'Scores': [85, 90, 78, 88, 76]}
df = pd.DataFrame(data)
plt.figure(figsize=(8, 5))
ax = sns.barplot(x='Subjects', y='Scores', data=df, palette='viridis')
for p in ax.patches: plt.text(p.get_x() + p.get_width()/2, p.get_height(), f'{int(p.get_height())}', ha='center')
plt.title('Subject Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.grid()
plt.show()