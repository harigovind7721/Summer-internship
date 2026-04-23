import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2024-01-01", "2024-01-03", "2024-01-05", "2024-01-07",
        "2024-01-09", "2024-01-11", "2024-01-13", "2024-01-15",
        "2024-01-17", "2024-01-19", "2024-01-21", "2024-01-23",
        "2024-01-25", "2024-01-27", "2024-01-29", "2024-01-31"
    ],
    "Revenue": [
        5200, 4800, 6100, 7300, 5900, 8200, 7100, 6800,
        9100, 8400, 7600, 9800, 8700, 10200, 9500, 11000
    ]
})

print("=" * 55)
print("  STEP 1: Original DataFrame")
print("=" * 55)
print(df)
print("Date dtype:", df["Date"].dtype)

df["Date"] = pd.to_datetime(df["Date"])

print("\n" + "=" * 55)
print("  STEP 2: After pd.to_datetime()")
print("=" * 55)
print(df)
print("Date dtype:", df["Date"].dtype)

df["Year"]  = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"]   = df["Date"].dt.day

print("\n" + "=" * 55)
print("  STEP 3: Extracted Year, Month, Day")
print("=" * 55)
print(df)

df["Previous_Day_Revenue"] = df["Revenue"].shift(1)

print("\n" + "=" * 55)
print("  STEP 4: Previous_Day_Revenue using shift(1)")
print("=" * 55)
print(df[["Date", "Revenue", "Previous_Day_Revenue"]])
print("\n  Note: First row is NaN — no previous day exists")

df["Revenue_Change"] = df["Revenue"].diff()

print("\n" + "=" * 55)
print("  STEP 5: Revenue_Change using diff()")
print("=" * 55)
print(df[["Date", "Revenue", "Previous_Day_Revenue", "Revenue_Change"]])
print("\n  Positive = revenue increased | Negative = revenue dropped")


df = df.set_index("Date")

print("\n" + "=" * 55)
print("  STEP 6: After set_index('Date')")
print("=" * 55)
print(df)

retrieved = df.loc["2024-01-15", "Revenue"]

print("\n" + "=" * 55)
print("  STEP 7: Indexing → Revenue on 2024-01-15")
print("=" * 55)
print("df.loc['2024-01-15', 'Revenue'] =", retrieved)

weekly = df[["Revenue"]].resample("W").sum()

print("\n" + "=" * 55)
print("  STEP 8: Weekly Revenue Total — resample('W').sum()")
print("=" * 55)
print(weekly)


monthly = df[["Revenue"]].resample("ME").sum()

print("\n" + "=" * 55)
print("  STEP 9: Monthly Revenue Total — resample('ME').sum()")
print("=" * 55)
print(monthly)

print("\n" + "=" * 55)
print("  FINAL SUMMARY")
print("=" * 55)
print(f"  Total Days Recorded  : {len(df)}")
print(f"  Total Revenue (Jan)  : ₹{df['Revenue'].sum():,.0f}")
print(f"  Highest Revenue Day  : {df['Revenue'].idxmax().date()} → ₹{df['Revenue'].max():,.0f}")
print(f"  Lowest Revenue Day   : {df['Revenue'].idxmin().date()} → ₹{df['Revenue'].min():,.0f}")
print(f"  Average Daily Revenue: ₹{df['Revenue'].mean():,.0f}")
print("=" * 55)