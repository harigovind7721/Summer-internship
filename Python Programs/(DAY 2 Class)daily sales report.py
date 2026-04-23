unit_price = 150
quantity_sold = 40
sales_target = 8000

total_sales = unit_price * quantity_sold

quantity_sold += 20
total_sales += unit_price * 20

target_achieved = total_sales >= sales_target
valid_sale = target_achieved and quantity_sold > 0

print("========== DAILY SALES REPORT ==========")
print(f"Unit Price       : Rs.{unit_price}")
print(f"Quantity Sold    : {quantity_sold}")
print(f"Sales Target     : Rs.{sales_target}")
print(f"Total Sales      : Rs.{total_sales}")
print(f"Target Achieved  : {target_achieved}")
print(f"Valid Sale Check : {valid_sale}")
print("=========================================")