import pandas as pd

# Create the sample dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(data)
print("\n")
# Part (a): Shape of the DataFrame
print("Shape of the DataFrame:", df.shape)
print("\n")
# Part (b): Summary of the DataFrame
print("\nSummary of the DataFrame:")
print(df.info())
print("\n")
# Part (c): Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())
print("\n")
# Part (d): Display first 5 rows and last 3 rows
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 3 rows:")
print(df.tail(3))
print("\n")
# Part (e):  statistics
average_salary = df["Salary"].mean()
total_bonus = df["Bonus"].sum()
youngest_age = df["Age"].min()
highest_rating = df["Rating"].max()
print("\n")
print("\nAverage Salary:", average_salary)
print("Total Bonus:", total_bonus)
print("Youngest Employee's Age:", youngest_age)
print("Highest Performance Rating:", highest_rating)
print("\n")
# Part (f): Sort by Salary in descending order
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nDataFrame sorted by Salary (descending):")
print(sorted_df)
print("\n")
# Part (g): Add a new column categorizing employees based on performance rating
df["Performance"] = pd.cut(
    df["Rating"],
    bins=[0, 4.0, 4.5, 5.0],
    labels=["Average", "Good", "Excellent"]
)
print("\nDataFrame with Performance column:")
print(df[["Name", "Performance"]])
print("\n")
# Part (h): Check for missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())
print("\n")
# Part (i): Rename Employee_ID to ID
df.rename(columns={"Employee_ID": "ID"}, inplace=True)
print("\nDataFrame with renamed column:")
print(df)
print("\n")
# Part (j): Filter employees with specific criteria
filtered_employees = df[(df["Years_of_Experience"] > 5) & (df["Department"] == "IT")]
print("\nFiltered employees (more than 5 years of experience in IT):")
print(filtered_employees)
print("\n")
# Part (k): Add a new column 'Tax' (10% of Salary)
df["Tax"] = df["Salary"] * 0.1
print("\nDataFrame with Tax column:")
print(df)
print("\n")
# Part (l): Save the modified DataFrame to a CSV file
df.to_csv("modified_employees.csv", index=False)
print("\nModified DataFrame saved to 'modified_employees.csv'.")
