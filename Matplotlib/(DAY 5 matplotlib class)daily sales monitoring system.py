import numpy as np
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = np.array([100, 150, np.nan, 200, 250])

max_idx = int(np.nanargmax(sales))

plt.plot(days, sales, color="blue", linestyle="--", marker="o", label="Sales")
plt.plot(days[max_idx], sales[max_idx], "ro", markersize=12, label="Highest Sale")

plt.title("Daily Sales Report")
plt.xlabel("Day")
plt.ylabel("Sales Amount")
plt.legend()
plt.tight_layout()
plt.show()