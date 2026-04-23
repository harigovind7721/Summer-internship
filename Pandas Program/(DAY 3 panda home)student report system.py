import pandas as pd
import numpy as np

data = {
    "EmpID": [101, 102, 103, 104, 105, 106],
    "Name": ["Arun", "Divya", "John", "Meenu", "Rahul", "Sara"],
    "Company": ["TCS", "TCS", "Infosys", "Infosys", "Wipro", "Wipro"],
    "Year": [2023, 2024, 2023, 2024, 2023, 2024],
    "Salary": [45000, 48000, np.nan, 52000, 41000, 46000],
    "Role": ["Developer", "Tester", "Developer", "HR", np.nan, "Tester"]
}

df = pd.DataFrame(data)

print(df.head(3))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df.isnull())
print(df.isnull().sum())

df["Company"] = df["Company"].astype("category")
df["Role"] = df["Role"].astype("category")

print(df.dtypes)

df_multi = df.set_index(["Company", "Year"])

print(df_multi)
print(df_multi.index)
print(df_multi.head())