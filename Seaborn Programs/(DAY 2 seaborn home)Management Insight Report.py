import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="time")
plt.show()

sns.violinplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill by Day")
plt.show()

sns.stripplot(data=tips, x="day", y="total_bill")
plt.title("Individual Bills per Day")
plt.show()

sns.swarmplot(data=tips, x="day", y="total_bill")
plt.title("Bills per Day (Swarm)")
plt.show()

sns.displot(data=tips, x="total_bill", col="time", kde=True)
plt.show()

sns.ecdfplot(data=tips, x="total_bill")
plt.title("ECDF of Total Bill")
plt.show()

sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Bill vs Tip with Regression Line")
plt.show()

sns.lmplot(data=tips, x="total_bill", y="tip", col="sex")
plt.show()