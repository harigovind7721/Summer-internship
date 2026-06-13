import pandas as pd

df = pd.read_csv("SuperStoreOrders.csv")

print("=== BEFORE CLEANING ===")
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Step 1: Fix sales — remove commas and convert to integer
df['sales'] = pd.to_numeric(df['sales'].str.replace(',', ''), errors='coerce')

# Step 2: Fix order_date and ship_date — convert to datetime (mixed formats)
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, format='mixed')
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, format='mixed')

# Step 3: Rebuild year column from order_date (original had 31,223 mismatches)
df['year'] = df['order_date'].dt.year

print("\n=== AFTER CLEANING ===")
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nSample:\n", df[['order_date', 'ship_date', 'year', 'sales']].head())

df.to_csv("SuperStoreOrders_cleaned.csv", index=False)
print("\nCleaned dataset saved as SuperStoreOrders_cleaned.csv")