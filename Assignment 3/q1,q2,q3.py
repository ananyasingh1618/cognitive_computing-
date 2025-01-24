import pandas as pd
data = {
    "Tid": [1,2,3,4,5,6,7,8,9,10],
    "Refund": ["yes", "no", "no", "yes", "no","no","yes","no","no","no"],
    "Marital Status": ["single","married","single","married","divorced","married","divorced","single","married","single"],
    "Taxable Income": [125000, 100000, 70000, 120000, 95000, 60000, 220000, 85000, 75000, 90000],
    "Cheat": ["NO", "NO", "NO", "NO", "YES", "NO","NO","YES", "NO", "YES"],
    
}
print("\n")
print("\n")
df = pd.DataFrame(data)
print(df)
print("\n")
print("\n")
# question 2

rows = df.iloc[[0, 4, 7, 8]]
print(rows)
print("\n")
print("\n")
#question 3
selected_rows = df.iloc[3:8]
print(selected_rows)
print("\n")
selected_data_1 = df.iloc[4:9, 2:5]  
print(selected_data_1)
print("\n")
selected_data_2 = df.iloc[:, 1:4]  # Column index 4 is exclusive, so this includes columns 1, 2, and 3
print(selected_data_2)
