import pandas as pd
data = {
    'EmpID':      [201, 202, 203, 204, 205, 206],
    'Name':       ['Arun','Neha','Sona','Rahul','Maya','John'],
    'Age':        [23, 29, 35, 27, 31, 26],
    'Dept':       ['IT','HR','IT','Finance','IT','HR'],
    'Salary':     [25000, 32000, 45000, 38000, 50000, 28000],
    'Attendance': [78, 88, 92, 85, 95, 60],
    'Status':     ['pending','completed','pending','completed','pending','pending'],
    'City':       ['Kochi','Trivandrum','New Delhi','Mumbai','New York','Yorkshire']
}
df = pd.DataFrame(data)
print(df[['Name', 'Salary']])
print(df.loc[3])
print(df.iloc[3])
print(df.loc[1:4, ['Name', 'Dept', 'Attendance']])

print(df[df['Salary'] > 35000])
print(df[(df['Dept'] == 'IT') & (df['Attendance'] >= 90)])
print(df[df['City'].str.contains('York')])

df['Bonus']       = df['Salary'] * 0.10
df['FinalSalary'] = df['Salary'] + df['Bonus']
df['Status']      = df['Status'].replace('pending', 'in progress')
df = df.drop(columns=['City'])
print(df.query("Age > 25 and Dept == 'IT'"))

df['AttendanceLevel'] = pd.cut(
    df['Attendance'],
    bins=[0, 70, 85, 100],
    labels=['Poor', 'Average', 'Excellent']
)
print(df[['Name', 'Attendance', 'AttendanceLevel']])

numeric_cols = df.select_dtypes(include='number')
result = numeric_cols.map(lambda x: x * 1)
print(result)