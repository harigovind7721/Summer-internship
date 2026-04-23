import pandas as pd


df = pd.DataFrame({
    "Date":  ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Sales": [100, 150, 120, 170, 200]
})

print("=" * 45)
print("  ORIGINAL DataFrame")
print("=" * 45)
print(df)
print("\nDate column dtype:", df["Date"].dtype)

df["Date"] = pd.to_datetime(df["Date"])

print("\n" + "=" * 45)
print("  AFTER pd.to_datetime()")
print("=" * 45)
print(df)
print("\nDate column dtype:", df["Date"].dtype)


df["Year"]  = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"]   = df["Date"].dt.day

print("\n" + "=" * 45)
print("  AFTER Extracting Year, Month, Day")
print("=" * 45)
print(df)

df["Previous_Day_Sales"] = df["Sales"].shift(1)

print("\n" + "=" * 45)
print("  AFTER shift(1) → Previous_Day_Sales")
print("=" * 45)
print(df)
print("\n  Note: First row is NaN — no previous day exists")

df["Daily_Change"] = df["Sales"].diff()

print("\n" + "=" * 45)
print("  AFTER diff() → Daily_Change")
print("=" * 45)
print(df)
print("\n  Note: First row is NaN — nothing to subtract from")

df = df.set_index("Date")

print("\n" + "=" * 45)
print("  AFTER set_index('Date')")
print("=" * 45)
print(df)

sales_jan03 = df.loc["2024-01-03", "Sales"]

print("\n" + "=" * 45)
print("  INDEXING → Sales on 2024-01-03")
print("=" * 45)
print("df.loc['2024-01-03', 'Sales'] =", sales_jan03)
print("=" * 45)