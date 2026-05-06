import matplotlib.pyplot as plt
import pandas as pd

dates = pd.date_range(start="2025-01-01", periods=5)
sales = [100, 120, 150, 180, 220]

plt.plot(dates, sales, marker="o", color="blue")
plt.title("Date-Based Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.show()

fig, ax1 = plt.subplots()

sales  = [100, 200, 300, 400]
profit = [20, 50, 90, 150]

ax1.plot(sales, color="blue", marker="o", label="Sales")
ax1.set_ylabel("Sales Amount", color="blue")

ax2 = ax1.twinx()           # creates second Y-axis sharing same X
ax2.plot(profit, color="green", marker="s", linestyle="--", label="Profit")
ax2.set_ylabel("Profit", color="green")

plt.title("Sales vs Profit")
plt.tight_layout()
plt.show()

x = [1, 2, 3, 4]
y = [10, 100, 1000, 10000]

plt.plot(x, y, marker="o", color="red")
plt.yscale("log")           # applies log scale to Y-axis
plt.title("Exponential Growth Analysis")
plt.xlabel("x")
plt.ylabel("y (log scale)")
plt.tight_layout()
plt.show()

weeks     = [1, 2, 3, 4]
product_a = [30, 40, 50, 60]
product_b = [20, 30, 40, 50]

plt.stackplot(weeks, product_a, product_b,
              labels=["Product A", "Product B"],
              alpha=0.7)
plt.title("Stacked Sales Contribution")
plt.xlabel("Week")
plt.ylabel("Sales Amount")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()