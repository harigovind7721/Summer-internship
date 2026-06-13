import seaborn as sns 
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
flights=sns.load_dataset("flights")
sns.set_style("whitegrid")
sns.set_context("talk")
custom_colors=["#FF9999", "#66B2FF"]
plt.figure(figsize=(8, 5))
sns.countplot(data=tips,x="day", hue="day",palette="Set2",legend=False)
plt.title("Customer Count by Day")
plt.xlabel("Day")
plt.ylabel("Number of customers")
plt.show()
plt.figure(figsize=(10, 5))
flights_pivot=flights.pivot(index="year", columns="months", values="passengers")
sns.lineplot(data=flights_pivot, palette="Blues")
plt.title("Passengers growth over years ")
plt.xlabel("Years")
plt.ylabel("Passengers")
plt.show()
plt.figure(figsize=(6, 5))
sns.countplot(data=tips,x="smoker",hue="smoker",
              palette=custom_colors, legend=False)
plt.title("Smoker vs Non-Smoker Count")
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips,
                x="total_bill",
                y="tip",
                hue="time",
                palette="coolwarm",
                s=100)
plt.title("Totally Bill vs Tip (Lunch vs Dinner)")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()