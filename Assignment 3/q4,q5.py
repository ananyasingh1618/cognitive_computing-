import pandas as pd
file_path = "/Users/ananyasingh/cognitive__computing/cognitive_computing-/Assignment 3/Iris.csv"
df_csv = pd.read_csv(file_path)
print(df_csv.head())
print("\n")
print("\n")
# question 5
df_dropped = df_csv.drop(index=4).drop(columns=df_csv.columns[3])
print("\nDataFrame after deleting row 4 and column 3:")
print(df_dropped.head())