import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
n = 244
tips = pd.DataFrame({
    "total_bill": np.concatenate([
        np.random.normal(17, 6, 100),
        np.random.normal(21, 8, 144),
    ]).clip(3, 55),
    "tip":    np.random.uniform(1, 9, n),
    "sex":    np.random.choice(["Male", "Female"], n),
    "smoker": np.random.choice(["Yes", "No"], n),
    "day":    np.random.choice(["Thur","Fri","Sat","Sun"], n,
                               p=[0.25, 0.10, 0.35, 0.30]),
    "time":   ["Lunch"]*100 + ["Dinner"]*144,
    "size":   np.random.choice([1,2,3,4,5,6], n),
})

# Global theme & colour palette
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
COLOURS = {"Lunch": "#4C9BE8", "Dinner": "#E8834C"}

g = sns.FacetGrid(
    tips,
    col="time",
    col_order=["Lunch", "Dinner"],
    height=5,
    aspect=1.35,
    sharey=False,
)

g.map_dataframe(
    sns.histplot,
    x="total_bill",
    bins=16,
    kde=True,
    edgecolor="white",
    linewidth=0.6,
)

for ax, label in zip(g.axes.flat, ["Lunch", "Dinner"]):
    colour = COLOURS[label]
    for patch in ax.patches:
        patch.set_facecolor(colour)
        patch.set_alpha(0.78)
    for line in ax.lines:
        line.set_color(colour)
        line.set_linewidth(2.2)
    ax.set_xlabel("Total Bill ($)", fontsize=12, labelpad=6)
    ax.set_ylabel("Number of Customers", fontsize=12, labelpad=6)
    ax.tick_params(labelsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

g.set_titles(col_template="{col_name} Service", size=14, fontweight="bold")
g.figure.suptitle(
    "Customer Spending Distribution: Lunch vs Dinner",
    fontsize=16, fontweight="bold", y=1.05,
)
g.figure.tight_layout()
plt.show()

day_order = ["Thur", "Fri", "Sat", "Sun"]

fig = sns.catplot(
    data=tips,
    kind="box",
    x="day",
    y="total_bill",
    hue="time",
    order=day_order,
    hue_order=["Lunch", "Dinner"],
    palette=COLOURS,
    height=5.5,
    aspect=1.65,
    width=0.52,
    linewidth=1.4,
    flierprops=dict(marker="o", markersize=4, linestyle="none",
                    markerfacecolor="grey", alpha=0.5),
)

ax = fig.ax
ax.set_title(
    "Total Bill Distribution by Day  ·  Lunch vs Dinner",
    fontsize=15, fontweight="bold", pad=14,
)
ax.set_xlabel("Day of the Week", fontsize=12, labelpad=8)
ax.set_ylabel("Total Bill ($)", fontsize=12, labelpad=8)
ax.tick_params(labelsize=11)
ax.yaxis.grid(True, linestyle="--", linewidth=0.7, alpha=0.55)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

legend = fig._legend
legend.set_title("Service", prop={"size": 11, "weight": "bold"})
for text in legend.get_texts():
    text.set_fontsize(10)
legend.get_frame().set_linewidth(0.8)

fig.figure.tight_layout()
plt.show()