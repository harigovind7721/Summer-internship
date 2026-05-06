import matplotlib.pyplot as plt
months=[1, 2, 3, 4]
product_a=[100,150,200,250]
product_b=[120,170,210,260]
fig, ax = plt.subplots()
ax.plot(months, product_a, color='blue',  linestyle='-',  marker='o', label='Product A')
ax.plot(months, product_b, color='red',   linestyle='--', marker='s', label='Product B')
ax.set_title('Monthly Product Sales Comparison', fontsize=16)
ax.set_xlabel('Months', fontsize=13)
ax.set_ylabel('Sales (Units)', fontsize=13)
ax.legend(fontsize=12)
ax.grid(True)
ax.set_ylim(0, 300)
ax.set_xticks([1, 2, 3, 4])                       
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr'], fontsize=12)
ax.tick_params(axis='y', labelsize=12)
plt.tight_layout()  
plt.show()