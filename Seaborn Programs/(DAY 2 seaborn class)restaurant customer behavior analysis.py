import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()

sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Total Bill per Day")
plt.show()

sns.countplot(data=tips, x="day")
plt.title("Number of Customers per Day")
plt.show()

sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Distribution of Total Bill by Day")
plt.show()

sns.histplot(data=tips, x="total_bill", bins=20)
plt.title("Distribution of Total Bill")
plt.show()

sns.kdeplot(data=tips, x="total_bill")
plt.title("Smoothed Distribution of Total Bill")
plt.show()