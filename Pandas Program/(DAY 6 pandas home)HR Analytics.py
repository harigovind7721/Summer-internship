import pandas as pd

emp_df = pd.DataFrame({
    'EmpID': [101, 102, 103, 104],
    'Name':  ['asha', 'ravi', 'kiran', 'meera'],
    'Dept':  ['IT', 'HR', 'IT', 'Finance']
})

salary_df = pd.DataFrame({
    'EmpID':  [101, 102, 103, 105],
    'Salary': [50000, 40000, 55000, 45000]
})

bonus_df = pd.DataFrame({
    'EmpID': [101, 102, 104],
    'Bonus': [5000, 3000, 4000]
})


df = pd.merge(emp_df, salary_df, on='EmpID', how='left')
df = pd.merge(df, bonus_df, on='EmpID', how='outer')


df['Salary'] = df['Salary'].fillna(0)
df['Bonus']  = df['Bonus'].fillna(0)


df['FinalSalary'] = df['Salary'] + df['Bonus']


print(df['Salary'].sum())
print(df['Salary'].mean())
print(df['FinalSalary'].max())
print(df['Name'].count())


df['Category'] = df['FinalSalary'].apply(
    lambda x: 'High'   if x >= 55000
         else 'Medium' if x >= 45000
         else 'Low'
)


dept_map = {'IT': 'Information Technology', 'HR': 'Human Resources', 'Finance': 'Finance Department'}
df['Dept'] = df['Dept'].map(dept_map)

df['Dept_Avg_FinalSalary'] = df.groupby('Dept')['FinalSalary'].transform('mean')


emp_indexed    = emp_df.set_index('EmpID')
salary_indexed = salary_df.set_index('EmpID')
joined_df = emp_indexed.join(salary_indexed, how='left')
print(joined_df)


jan_df = pd.DataFrame({'EmpID':[101,102],'Name':['asha','ravi'],'Salary':[50000,40000],'Month':['Jan','Jan']})
feb_df = pd.DataFrame({'EmpID':[103,104],'Name':['kiran','meera'],'Salary':[55000,45000],'Month':['Feb','Feb']})
monthly_df = pd.concat([jan_df, feb_df], ignore_index=True)
print(monthly_df)