import pandas as pd

df = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105, 106],
    "Name": ["Asha", "Ravi", "Neha", "Arun", "Priya", "Kiran"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male"],
    "Salary": [50000, 40000, 55000, 60000, 42000, 52000]
})

print(df)
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)
multi_agg = df.groupby("Department")["Salary"].agg(["sum", "mean", "max", "min"])
print(multi_agg)
named_agg = df.groupby("Department").agg(
    Total_Salary=("Salary", "sum"),
    Avg_Salary=("Salary", "mean"),
    Employee_Count=("EmpID", "count")
)

print(named_agg)
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print(pivot)
crosstab = pd.crosstab(df["Department"], df["Gender"])
print(crosstab)