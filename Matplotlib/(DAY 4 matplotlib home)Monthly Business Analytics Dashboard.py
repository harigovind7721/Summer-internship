import matplotlib.pyplot as plt
sales_data = [10, 20, 20, 30, 40, 40, 50]
plt.hist(sales_data,bins=4)
plt.title("Sales Distribution")

#Pie Chart
labels = ["Product A", "Product B", "Product C"]
sizes = [40, 35, 25]
explode=(0.1,0,0)
plt.pie(sizes,labels=labels,explode=explode)
plt.title("Market Share Analysis")

#Box Plot
salary = [20000, 25000, 30000, 35000, 80000]
plt.boxplot(salary)
plt.title( "Employee Salary Distribution")

#Error Bar
x = [1, 2, 3]
y = [10, 20, 30]
error = [2, 3, 4]
plt.title("Measurement with Error Range")
plt.errorbar(x,y,yerr=error,fmt='o')
plt.show()