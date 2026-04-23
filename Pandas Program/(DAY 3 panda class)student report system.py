import pandas as pd
import numpy as np

data = {
    "Name": ["Asha", "Ravi", "Kiran", "Meera", "Vikram", "Sona"],
    "Age": [24, 27, np.nan, 26, 32, 25],
    "Marks": [85, 90, 78, 88, np.nan, 75],
    "Gender": ["Female", "Male", "Male", "Female", "Male", "Female"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance"]
}

df = pd.DataFrame(data)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df.isnull())
print(df.isnull().sum())

df["Gender"] = df["Gender"].astype("category")
df["Department"] = df["Department"].astype("category")

print(df.dtypes)