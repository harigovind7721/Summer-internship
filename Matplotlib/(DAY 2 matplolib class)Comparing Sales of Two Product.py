import matplotlib.pyplot as plt
plt.title("Weekly Website Visitors Trend")
days= [1, 2, 3, 4]
visitors = [120, 150, 130, 180]
plt.plot(days,visitors)
plt.figure(figsize=(8,4))
plt.plot(days, visitors, marker='o', linestyle='--', color='blue', linewidth=2, markersize=8)
plt.xlabel("Day")
plt.ylabel("Number of Visitors")
plt.title("Daily Visitor Count")
plt.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()