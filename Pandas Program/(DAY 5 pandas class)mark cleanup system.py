import pandas as pd
import numpy as np

data = {
    'StudentID': [101, 102, 103, 104, 105, 106],
    'Name':      ['Asha', 'Ravi', 'Asha', 'Kiran', 'Meera', 'John'],
    'City':      ['mumbai', 'Delhi', 'mumbai', 'chennai', 'Kolkata', 'Delhi'],
    'Marks':     [85, np.nan, 85, 78, 90, 70],
    'Grade':     ['A', 'B', 'A', 'F', 'A', 'B'],
    'Status':    ['pending', 'pending', 'pending', 'completed', 'completed', 'pending']
}
df = pd.DataFrame(data)

print(df.isnull().sum())
df['Marks'] = df['Marks'].fillna(0)

df_clean = df.dropna()

df['Grade'] = df['Grade'].replace('F', 'Fail')

print(df.duplicated())
df = df.drop_duplicates()

df['City_Upper'] = df['City'].str.upper()

print(df[df['City'].str.contains('del', case=False)])

df = df.rename(columns={'Marks': 'Score'})
df['Score'] = df['Score'].astype(float)

print(df.sort_values('Score', ascending=False))
print(df.sort_index())

df = df.set_index('StudentID')
print(df)
df = df.reset_index()
print(df)