import pandas as pd

df = pd.DataFrame({
    "OrderID": [1,2,3,4,5,6,7],
    "Customer": ["Anu","Rahul","Meera","Ajay","Sara","Vishnu","Diya"],
    "City": ["Kochi","Kochi","Trivandrum","Kochi","Trivandrum","Kochi","Trivandrum"],
    "Category": ["Grocery","Electronics","Grocery","Clothing","Clothing","Grocery","Electronics"],
    "PaymentMode": ["UPI","Card","Cash","UPI","Card","Cash","UPI"],
    "Amount": [1200,25000,800,3500,4000,950,18000]
})

print(df)
category_sales = df.groupby("Category")["Amount"].sum()
print(category_sales)
city_category_avg = df.groupby(["City", "Category"])["Amount"].mean()
print(city_category_avg)
report = df.groupby("City").agg(
    Total_Sales=("Amount", "sum"),
    Avg_Sales=("Amount", "mean"),
    Order_Count=("OrderID", "count")
)

print(report)
pivot = pd.pivot_table(
    df,
    values="Amount",
    index="City",
    columns="PaymentMode",
    aggfunc="sum"
)

print(pivot)
crosstab = pd.crosstab(df["Category"], df["PaymentMode"])
print(crosstab)
melted = pivot.reset_index().melt(
    id_vars="City",
    var_name="PaymentMode",
    value_name="TotalAmount"
)

print(melted)
stacked = pivot.stack()
print(stacked)

unstacked = stacked.unstack()
print(unstacked)