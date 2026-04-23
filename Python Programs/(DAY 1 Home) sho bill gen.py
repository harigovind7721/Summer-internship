product_name = "Wireless Headphones"
price = "2499.99"
quantity = "3"
discount_percent = 10

price = float(price)
quantity = int(quantity)

total_amount = price * quantity
discount_amount = (discount_percent / 100) * total_amount
final_amount = total_amount - discount_amount

tax = service_charge = 0

print("========== ONLINE SHOPPING BILL ==========")
print(f"Product      : {product_name}")
print(f"Price        : Rs.{price:.2f}")
print(f"Quantity     : {quantity}")
print(f"Total Amount : Rs.{total_amount:.2f}")
print(f"Discount     : {discount_percent}% = Rs.{discount_amount:.2f}")
print(f"Tax          : Rs.{tax}")
print(f"Service Charge: Rs.{service_charge}")
print(f"Final Amount : Rs.{final_amount:.2f}")
print(f"Data Type of final_amount: {type(final_amount)}")
print("==========================================")