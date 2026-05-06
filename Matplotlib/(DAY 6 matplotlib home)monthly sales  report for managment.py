import matplotlib.pyplot as plt 
import numpy as np
months = [1, 2, 3, 4] 
sales_2024 = [200, 260, 300, 380] 
sales_2025 = [220, 280, 330, 420]
plt.figure(figsize=(8,4))
plt.plot(months, sales_2024, color="steelblue",  linewidth=2, alpha=0.7, marker="o", label="2024")
plt.plot(months, sales_2025, color="darkorange", linewidth=2, alpha=0.7, marker="s", label="2025")
plt.title('Monthly Sales Comparison (2024 vs 2025)')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.savefig('sales_report.png', dpi=200)
np.random.seed(42)
x = np.random.rand(100) * 100
y = np.random.rand(100) * 100
intensity = np.random.rand(100) * 100  # for color
plt.figure()
scatter = plt.scatter(x, y, c=intensity, cmap='viridis', alpha=0.7)
plt.colorbar(scatter, label='Sales Intensity')
plt.title('Sales Intensity Distribution')
plt.xlabel('Region Index')
plt.ylabel('Sales Value')
x = [1, 2, 3, 4]
y = [10, 20, 25, 40]
plt.figure(figsize=(8, 4), dpi=300)
plt.plot(x, y, marker='o')
plt.title('Report Line Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.savefig('report_chart.pdf')
plt.savefig('report_chart.svg')
plt.show()