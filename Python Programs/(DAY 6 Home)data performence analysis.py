def classify_sales(amount):
    if amount >= 100000:
        return "High Performance"
    elif amount >= 50000:
        return "Average Performance"
    else:
        return "Low Performance"

calculate_bonus = lambda amount: amount * 0.05

def total_sales(sales_list, index=0):
    if index == len(sales_list):
        return 0
    return sales_list[index] + total_sales(sales_list, index + 1)

n = int(input("Enter number of months: "))
sales = []

for i in range(n):
    amount = float(input(f"Enter sales for month {i + 1}: "))

    if amount < 0:
        print("Negative sales entered. Stopping input.")
        break

    if amount == 0:
        print(f"Month {i + 1}: No sales recorded, skipped.")
        continue

    sales.append(amount)

print("\n--- Month-wise Report ---")
for i, amount in enumerate(sales):
    category = classify_sales(amount)
    bonus = calculate_bonus(amount)
    print(f"Month {i + 1}: Rs.{amount:.2f} | {category} | Bonus: Rs.{bonus:.2f}")

print(f"\nTotal Sales: Rs.{total_sales(sales):.2f}")