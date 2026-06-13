import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
sns.set_theme()
tips=sns.load_dataset("tips")
print("=== First 5 Rows of the Tips Dataset ===")
print(tips.head())

plt.figure(figsize=(8, 5))
sns.histplot(data=tips, x="total_bill", bins=20, kde=True, color="steelblue")
plt.title("Distribution of Total Bill", fontsize=14, fontweight='bold')
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill",
            hue="day", palette="Set2", legend=False)
plt.title("Total Bill by Day of the Week", fontsize=14, fontweight='bold')
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x="day",
              hue="day", palette="muted", legend=False)
plt.title("Number of Customers per Day", fontsize=14, fontweight='bold')
plt.xlabel("Day")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()