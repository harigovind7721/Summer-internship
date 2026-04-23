monthly_sales=(12000, 15000, 11000, 18000, 16000, 14000)
print("Sales Data",monthly_sales)
print("Total Months",len(monthly_sales))

print("\n===== Accessing Elements =====")
print("First month    :", monthly_sales[0])
print("Last month     :", monthly_sales[-1])
print("Index 1 to 4   :", monthly_sales[1:5])

print("\n===== Membership Check =====")
if 15000 in monthly_sales:
    print("15000 exists in the tuple : True")
else:
    print("15000 exists in the tuple : False")

print("\n===== Membership Check =====")
if 15000 in monthly_sales:
    print("15000 exists in the tuple : True")
else:
    print("15000 exists in the tuple : False")    

print("\n===== Monthly Sales (for loop) =====")
for index, sale in enumerate(monthly_sales):
    print(f"  Month {index + 1} : ₹{sale}")

print("\n===== Convert → Update → Convert Back =====")
sales_list = list(monthly_sales)
print("As list              :", sales_list)
 
sales_list.append(17000)
print("After append(17000)  :", sales_list)
 
sales_list.remove(11000)
print("After remove(11000)  :", sales_list)
 
monthly_sales = tuple(sales_list)
print("Back to tuple        :", monthly_sales)

print("\n===== Tuple Unpacking =====")
first, second, *remaining = monthly_sales
print("First month    :", first)
print("Second month   :", second)
print("Remaining      :", remaining)

print("\n===== Sorted Sales =====")
sorted_sales = sorted(monthly_sales)
print("Ascending      :", sorted_sales)
print("Descending     :", sorted(monthly_sales, reverse=True))

print("\n===== Sales Summary =====")
print("Highest Sales  : ₹", max(monthly_sales))
print("Lowest Sales   : ₹", min(monthly_sales))