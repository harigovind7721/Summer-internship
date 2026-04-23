import pandas as pd
data = {
    'StudentID': [101, 102, 103, 104, 105],
    'Name':      ['Asha', 'Ravi', 'Kiran', 'Meera', 'John'],
    'Age':       [24, 30, 28, 26, 22],
    'Dept':      ['HR', 'IT', 'IT', 'Finance', 'IT'],
    'Marks':     [78, 90, 84, 92, 65],
    'Status':    ['pending', 'completed', 'pending', 'completed', 'pending'],
    'City':      ['New Delhi', 'Mumbai', 'New York', 'New Delhi', 'Yorkshire']
}
df = pd.DataFrame(data)
df_orig = df.copy()
print("=" * 50)
print("ORIGINAL DATAFRAME")
print("=" * 50)
print(df)
print("=" * 50)
print("______Only name_____\n",df['Name'])
print("=" * 50)
print("_______Name and Marks________\n",df[['Name','Marks']])
print("=" * 50)
print("______Row with index 0______\n",df.loc[0])
print("=" * 50)
print("__________Marks of index 1___________\n",df.loc[1,'Marks'])
print("=" * 50)
print("______________Name and dept_____________\n",df.loc[:,['Name','Dept']])
print("=" * 50)
print("_______3rd Row______\n",df.iloc[2])
print("=" * 50)
print("_______2nd row 5th______\n",df.iloc[1,4])
print("=" * 50)
print("_________Name and marks________\n",df.iloc[:,[1,4]])
print("=" * 50)
print("________Rows 0 to 2, columns Name and Marks_______\n",df.loc[0:2, ['Name', 'Marks']])
print("=" * 50)
print("__________First 3 rows___________\n",df.iloc[0:3])
print("=" * 50)
print("_________print(df[df['Marks'] >= 85])________\n",df[df['Marks'] >= 85])
print("=" * 50)
print(df[(df['Dept'] == 'IT') & (df['Age'] > 25)])
print("=" * 50)
print("\n" + "=" * 50)
print("6. QUERY USING query()")
print("=" * 50)
print("\n-- Marks >= 80 and Dept == 'IT' --")
print(df.query('Marks >= 80 and Dept == "IT"'))
print("\n" + "=" * 50)
print("7. TRANSFORMATION")
print("=" * 50) 
print("\n-- Add BonusMarks = Marks + 5 --")
df['BonusMarks'] = df['Marks'] + 5
print(df[['Name', 'Marks', 'BonusMarks']]) 
print("\n-- Update Status: 'pending' → 'in progress' --")
df['Status'] = df['Status'].replace('pending', 'in progress')
print(df[['Name', 'Status']])
print("\n-- Drop column City --")
df = df.drop(columns=['City'])
print(df.columns.tolist())

print("\n-- map(): multiply numeric columns by 1 --")
numeric_cols = df.select_dtypes(include='number')
print(numeric_cols.map(lambda x: x * 1))

print("\n" + "=" * 50)
print("8. STRING OPERATIONS")
print("=" * 50)
print("\n-- Cities containing 'York' (from original df) --")
print(df_orig[df_orig['City'].str.contains('York')])
print("\n" + "=" * 50)
print("9. BINNING USING cut()")
print("=" * 50)
print("\n-- Performance: 0-70=Low, 70-85=Average, 85-100=High --")
df['Performance'] = pd.cut(
    df['Marks'],
    bins=[0, 70, 85, 100],
    labels=['Low', 'Average', 'High']
)
print(df[['Name', 'Marks', 'Performance']])