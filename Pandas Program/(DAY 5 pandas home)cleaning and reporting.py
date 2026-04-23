import pandas as pd
import numpy as np

data = {
    'OrderID':      [1, 2, 3, 4, 5, 6],
    'CustomerName': ['Arun','Neha','Arun','Sona','Rahul','Maya'],
    'Product':      ['Apple Juice','Mango Shake','Apple Juice',
                     'Orange Juice','Banana Smoothie','Apple Juice'],
    'Qty':          [2, np.nan, 2, 1, 3, 1],
    'Price':        [120, 150, 120, np.nan, 200, 120],
    'City':         ['kochi','Delhi','kochi','Mumbai','Chennai','new york'],
    'Status':       ['pending','completed','pending','pending','completed','pending']
}
df = pd.DataFrame(data)

df['Qty']   = df['Qty'].fillna(1)
df['Price'] = df['Price'].fillna(0)


df_dropped = df.dropna()


print(df.duplicated())
df = df.drop_duplicates()


df['City_Upper'] = df['City'].str.upper()
juice_orders = df[df['Product'].str.contains('Juice')]
print(juice_orders)

df = df.rename(columns={'CustomerName': 'Customer', 'Qty': 'Quantity'})
df['Quantity'] = df['Quantity'].astype(int)
df['Price']    = df['Price'].astype(float)


df['Status'] = df['Status'].replace('pending', 'in progress')

print(df.sort_values('Price', ascending=False))
df = df.set_index('OrderID')
print(df)
df = df.reset_index()
print(df.sort_index())