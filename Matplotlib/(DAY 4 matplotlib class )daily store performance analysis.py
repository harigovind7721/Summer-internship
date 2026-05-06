import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
sales = [100, 120, 140, 130, 160]
plt.plot(days,sales,marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

#_____Bar Chart___
categories = ["Electronics", "Clothing", "Grocery"]
values = [50, 30, 40]
plt.bar(categories,values)
plt.title("Category-wise Sales")
plt.show()

#_____Scatter Chart_____
age = [22, 25, 30, 35, 40]
purchase = [200, 400, 600, 650, 800]
plt.scatter(age,purchase)
plt.title("Customer Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchhase Amount")
plt.show()