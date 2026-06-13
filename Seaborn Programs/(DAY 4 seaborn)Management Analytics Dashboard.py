import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

tips = sns.load_dataset("tips")   
iris = sns.load_dataset("iris")


PALETTE_SPECIES = {"setosa": "#2196F3", "versicolor": "#4CAF50", "virginica": "#FF5722"}
PALETTE_SMOKER  = {"Yes": "#E53935", "No": "#A04E43"}
BG, GRID_C = "#F8F9FB", "#DEE2E6"

plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG,
    "axes.edgecolor": "#CED4DA", "axes.labelcolor": "#343A40",
    "xtick.color": "#495057", "ytick.color": "#495057",
    "text.color": "#212529", "font.family": "DejaVu Sans",
    "axes.titleweight": "bold", "axes.titlesize": 13,
    "axes.labelsize": 11, "xtick.labelsize": 9, "ytick.labelsize": 9,
})

pp = sns.pairplot(
    iris,
    hue="species",
    palette=PALETTE_SPECIES,
    diag_kind="kde",
    plot_kws=dict(alpha=0.65, s=55, edgecolor="white", linewidth=0.4),
    diag_kws=dict(linewidth=2, fill=True, alpha=0.35),
    height=2.4,
    aspect=1.05,
)

nice_labels = {
    "sepal_length": "Sepal Length (cm)", "sepal_width": "Sepal Width (cm)",
    "petal_length": "Petal Length (cm)", "petal_width": "Petal Width (cm)",
}
for ax in pp.axes.flat:
    if ax is None: continue
    ax.set_facecolor(BG)
    ax.grid(True, color=GRID_C, linewidth=0.6, linestyle="--")
    ax.set_axisbelow(True)
    xl, yl = ax.get_xlabel(), ax.get_ylabel()
    if xl in nice_labels: ax.set_xlabel(nice_labels[xl])
    if yl in nice_labels: ax.set_ylabel(nice_labels[yl])

pp.figure.suptitle(
    "Iris Dataset  ·  Pairwise Feature Relationships by Species",
    fontsize=15, fontweight="bold", y=1.015,
)
handles = [mpatches.Patch(facecolor=c, label=s.capitalize(), edgecolor="white")
           for s, c in PALETTE_SPECIES.items()]
pp.figure.legend(handles=handles, title="Species", loc="upper right",
                 bbox_to_anchor=(1.0, 1.0), frameon=True, framealpha=0.9,
                 title_fontsize=10, fontsize=9)
pp._legend.remove()
pp.figure.set_size_inches(12, 10)
pp.figure.tight_layout()
plt.show()


top_row  = tips.loc[tips["tip"].idxmax()]
col_map  = {"Lunch": 0, "Dinner": 1}
row_map  = {"Male": 0, "Female": 1}

fg = sns.relplot(
    data=tips, x="total_bill", y="tip",
    row="sex", col="time",
    hue="smoker", palette=PALETTE_SMOKER, hue_order=["Yes", "No"],
    kind="scatter", alpha=0.70, s=65, edgecolor="white", linewidth=0.5,
    height=4.0, aspect=1.25,
    facet_kws=dict(sharey=True, sharex=True, margin_titles=True),
)

for ax in fg.axes.flat:
    ax.set_facecolor(BG)
    ax.grid(True, color=GRID_C, linewidth=0.65, linestyle="--")
    ax.set_axisbelow(True)
    ax.set_xlabel("Total Bill ($)", labelpad=5)
    ax.set_ylabel("Tip Amount ($)", labelpad=5)
    ax.xaxis.set_major_formatter(mticker.FormatStrFormatter("$%.0f"))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("$%.1f"))
    plt.setp(ax.get_xticklabels(), rotation=35, ha="right")


ann_ax = fg.axes[row_map[top_row["sex"]], col_map[top_row["time"]]]
ann_ax.annotate(
    f" Highest Tip\n ${top_row['tip']:.2f}",
    xy=(top_row["total_bill"], top_row["tip"]),
    xytext=(top_row["total_bill"] - 12, top_row["tip"] - 1.5),
    fontsize=9, fontweight="bold", color="#B71C1C",
    arrowprops=dict(arrowstyle="-|>", color="#B71C1C", lw=1.4,
                    connectionstyle="arc3,rad=-0.2"),
    bbox=dict(boxstyle="round,pad=0.35", fc="#FFEBEE", ec="#E53935", lw=1),
)

fg.set_titles(row_template="{row_name}", col_template="{col_name}",
              size=12, fontweight="bold")
fg.figure.suptitle(
    "Tip vs Total Bill  ·  Segmented by Gender, Meal Time & Smoking Status",
    fontsize=14, fontweight="bold", y=1.03,
)
leg = fg.legend
leg.set_title("Smoker", prop={"size": 10, "weight": "bold"})
leg.get_frame().set_facecolor(BG)
fg.figure.tight_layout()
plt.show()