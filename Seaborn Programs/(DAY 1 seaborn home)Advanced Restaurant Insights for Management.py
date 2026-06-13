import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")


tips["tip_percentage"] = (tips["tip"] / tips["total_bill"]) * 100

print(tips.head())          # see first 5 rows
print(tips.dtypes)          # check column types


sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", palette="pastel")
plt.title("Total Bill vs Tip")
plt.show()


sns.boxplot(data=tips, x="sex", y="total_bill", hue="sex",
            palette="pastel", legend=False)
plt.title("Total Bill by Gender")
plt.show()


sns.violinplot(data=tips, x="sex", y="tip_percentage", hue="sex",
               palette="pastel", inner="quartile", legend=False)
plt.title("Tip Percentage by Gender")
plt.show()


sns.relplot(data=tips, x="total_bill", y="tip",
            col="time", hue="sex", palette="pastel")
plt.show()