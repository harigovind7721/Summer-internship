import matplotlib.pyplot as plt


months    = [1, 2, 3, 4]
product_a = [200, 250, 300, 350]
product_b = [180, 220, 260, 310]



fig, ax = plt.subplots()

ax.plot(months, product_a, color='green', linestyle='-', marker='o', label='Product A')

ax.plot(months, product_b, color='red', linestyle='--', marker='s', label='Product B')

ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_title('Product A vs Product B')
ax.legend()   

plt.show()   
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)


ax1.plot(months, product_a, color='green', marker='o')
ax1.set_ylabel('Sales')
ax1.set_title('Product A')


ax2.plot(months, product_b, color='red', linestyle='--', marker='s')
ax2.set_xlabel('Month')   
ax2.set_ylabel('Sales')
ax2.set_title('Product B')

plt.tight_layout() 