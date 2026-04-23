mobile_buyers = {"C101", "C102", "C103", "C104"}
laptop_buyers = {"C103", "C104", "C105", "C106"}

print("Both Mobile & Laptop:", mobile_buyers & laptop_buyers)
print("Only Mobile Buyers:", mobile_buyers - laptop_buyers)
print("Only Laptop Buyers:", laptop_buyers - mobile_buyers)
print("Total Unique Customers:", mobile_buyers | laptop_buyers)

mobile_buyers.discard("C102")
print("Mobile Buyers after cancellation:", mobile_buyers)


customers = {
    "C101": {"name": "Arun", "city": "Kochi", "total_purchase": 45000},
    "C102": {"name": "Meera", "city": "Trivandrum", "total_purchase": 60000},
    "C103": {"name": "Rahul", "city": "Kollam", "total_purchase": 75000},
    "C104": {"name": "Sneha", "city": "Kottayam", "total_purchase": 30000}
}

print("\nCustomer IDs:")
for cid in customers:
    print(cid)

print("\nCustomers with purchase above ₹50,000:")
for cid, details in customers.items():
    if details["total_purchase"] > 50000:
        print(cid, "-", details)

customers["C105"] = {"name": "Anu", "city": "Alappuzha", "total_purchase": 52000}
customers.pop("C104")

customers_copy = customers.copy()
customers.clear()

print("\nCopied Dictionary:", customers_copy)
print("Original Dictionary after clear:", customers)