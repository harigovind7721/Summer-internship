import pandas as pd


df_dict = pd.DataFrame({
    "Name": ["Asha", "Ravi", "Meera"],
    "Age": [24, 30, 26],
    "Dept": ["HR", "IT", "Finance"]
})
print(df_dict)


csv_data = """Name,Age,Grade,Subject
Alice,20,A,Math
Bob,21,B,Science
Charlie,22,A,English"""

with open("students.csv", "w") as f:
    f.write(csv_data)

df_csv = pd.read_csv("students.csv")
print(df_csv)


df_excel_write = pd.DataFrame({
    "Name": ["Asha", "Ravi", "Meera"],
    "Age": [24, 30, 26],
    "Department": ["HR", "IT", "Finance"],
    "Salary": [35000, 50000, 40000]
})
df_excel_write.to_excel("employees.xlsx", index=False)

df_excel = pd.read_excel("employees.xlsx")
print(df_excel)


import json

json_data = [
    {"Name": "Arun", "Age": 22, "Grade": "A"},
    {"Name": "Binu", "Age": 21, "Grade": "B"}
]

with open("data.json", "w") as f:
    json.dump(json_data, f)

df_json = pd.read_json("data.json")
print(df_json)