import pandas as pd
student_df=pd.DataFrame({
    'StudentID':[1,2,3,4],
    'Name':['alice','bob','charlie','diya'],
    'Dept':['IT','HR','IT','FINANCE']
})

marks_df=pd.DataFrame({
    'StudentID':[1,2,3,4],
    'Math':[80,45,90,70],
    'Science':[75, 60, 88, 65]
})

inner_df = pd.merge(student_df, marks_df, on='StudentID', how='inner')
left_df  = pd.merge(student_df, marks_df, on='StudentID', how='left')
df = inner_df.copy()

df['Total'] = df['Math'] + df['Science']

print(df[['Math', 'Science']].sum())
print(df[['Math', 'Science']].mean())
print(df['Total'].min(), df['Total'].max())

df['Result'] = df['Total'].apply(lambda x: 'Pass' if x >= 150 else 'Fail')
df['Name'] = df['Name'].map(str.title)
df['Dept_Avg_Total'] = df.groupby('Dept')['Total'].transform('mean')

print(df)
week1_df = pd.DataFrame({
    'Name': ['Alice', 'Bob'], 'Math': [80, 45], 'Science': [75, 60]
})
week2_df = pd.DataFrame({
    'Name': ['Charlie', 'Diya'], 'Math': [90, 70], 'Science': [88, 65]
})
combined_df = pd.concat([week1_df, week2_df], ignore_index=True)
print(combined_df)