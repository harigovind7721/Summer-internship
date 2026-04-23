import pandas as pd
sales_series=pd.Series([250, 300, 150, 400, 350],index=["mon","tue","wed","thu","fri"])
print(sales_series)
print(sales_series["wed"])
print(sales_series.sum())
print(sales_series.mean())

sales_df = pd.DataFrame({"Day": ["mon", "tue", "wed", "thu", "fri"], "Sales": [250, 300, 150, 400, 350]})

print(sales_df)
print(sales_df["Sales"].max())
print(sales_df["Sales"].min())