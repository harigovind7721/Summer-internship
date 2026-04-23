import pandas as pd
import os


data = {
    "order_id": list(range(1, 101)),
    "product":  (["Notebook", "Mouse", "Chair", "Pen", "Keyboard"] * 20),
    "category": (["Stationery", "Electronics", "Furniture", "Stationery", "Electronics"] * 20),
    "price":    ([45, 850, 8500, 30, 1500] * 20),
    "quantity": ([1, 3, 2, 5, 4, 1, 2, 6, 3, 1] * 10),
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
print("sales_data.csv created with 100 rows")


filtered_chunks = []

for chunk in pd.read_csv("sales_data.csv", chunksize=10):
    filtered = chunk[chunk["quantity"] > 2]
    filtered_chunks.append(filtered)

print("All chunks processed")


combined_df = pd.concat(filtered_chunks, ignore_index=True)
print("Total rows after filter:", len(combined_df))


sample_df = combined_df.sample(n=50, random_state=42).reset_index(drop=True)
print("Random sample of 50 rows taken")


sample_df.to_csv("filtered_sales.csv", index=False)
print("filtered_sales.csv saved")

sample_df.to_excel("filtered_sales.xlsx", index=False, sheet_name="Filtered_Sales")
print("filtered_sales.xlsx saved")

sample_df.to_json("filtered_sales.json", orient="records", indent=4)
print("filtered_sales.json saved")