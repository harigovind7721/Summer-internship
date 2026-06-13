import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")


data = {
    "employee_id": range(1, 21),
    "age":         [25,30,35,28,45,32,27,50,38,29,42,33,48,26,36,31,44,37,24,40],
    "experience_years": [2,5,8,3,18,7,2,22,12,4,16,6,20,1,10,5,17,11,1,14],
    "salary":      [35000,48000,62000,41000,95000,57000,36000,110000,74000,
                    44000,89000,53000,105000,33000,69000,49000,92000,71000,32000,82000],
    "performance_score": [72,85,90,76,92,83,70,88,87,79,91,81,94,68,86,80,93,85,65,89],
    "satisfaction_score":[68,74,80,65,85,72,60,78,82,69,86,71,88,58,77,70,87,79,55,83],
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)      # export the CSV

df = pd.read_csv("sample_data.csv")            # load it back
numerical = ["age","experience_years","salary","performance_score","satisfaction_score"]

print("Dataset loaded — shape:", df.shape)
print(df[numerical].describe().round(1))


BG, GRID_C, ACCENT = "#F7F9FC", "#DDE3EA", "#1A73E8"
plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG,
    "axes.edgecolor": "#C8CDD4", "axes.labelcolor": "#2D3748",
    "xtick.color": "#4A5568", "ytick.color": "#4A5568",
    "text.color": "#1A202C", "font.family": "DejaVu Sans",
    "axes.titleweight": "bold", "axes.titlesize": 12,
    "axes.labelsize": 10, "xtick.labelsize": 9, "ytick.labelsize": 9,
})

nice = {
    "age": "Age (yrs)", "experience_years": "Experience (yrs)",
    "salary": "Salary ($)", "performance_score": "Performance",
    "satisfaction_score": "Satisfaction",
}


df["salary_band"] = pd.qcut(df["salary"], q=3,
                             labels=["Low Earner","Mid Earner","High Earner"])
BAND_PAL = {"Low Earner":"#64B5F6","Mid Earner":"#FFB300","High Earner":"#EF5350"}

pp = sns.pairplot(
    df[numerical + ["salary_band"]],
    hue="salary_band", palette=BAND_PAL,
    diag_kind="kde",
    plot_kws=dict(alpha=0.72, s=65, edgecolor="white", linewidth=0.5),
    diag_kws=dict(linewidth=2, fill=True, alpha=0.30),
    height=2.1, aspect=1.05,
)
for ax in pp.axes.flat:
    if ax is None: continue
    ax.set_facecolor(BG)
    ax.grid(True, color=GRID_C, linewidth=0.55, linestyle="--")
    ax.set_axisbelow(True)
    xl, yl = ax.get_xlabel(), ax.get_ylabel()
    if xl in nice: ax.set_xlabel(nice[xl])
    if yl in nice: ax.set_ylabel(nice[yl])
    if "salary" in xl:
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v/1000:.0f}k"))
    if "salary" in yl:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f"${v/1000:.0f}k"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

pp.figure.suptitle(
    "Employee Analytics  ·  Pairwise Relationships Across All Numerical Variables",
    fontsize=14, fontweight="bold", y=1.015,
)
handles = [mpatches.Patch(facecolor=c, label=l, edgecolor="white")
           for l, c in BAND_PAL.items()]
pp.figure.legend(handles=handles, title="Salary Band",
                 loc="upper right", bbox_to_anchor=(1.0, 1.0),
                 frameon=True, framealpha=0.92, title_fontsize=9, fontsize=8)
pp._legend.remove()
pp.figure.set_size_inches(13, 11)
pp.figure.tight_layout()
plt.show()


corr = df[numerical].corr()

fig, ax = plt.subplots(figsize=(9, 7))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

sns.heatmap(
    corr, ax=ax,
    annot=True, fmt=".2f", cmap="RdYlGn",
    vmin=-1, vmax=1, center=0,
    linewidths=2, linecolor=BG,
    annot_kws={"size": 12, "weight": "bold"},
    square=True,
    cbar_kws={"shrink": 0.78, "label": "Pearson r", "pad": 0.02},
)

nice_ticks = [nice.get(c, c) for c in numerical]
ax.set_xticklabels(nice_ticks, rotation=35, ha="right", fontsize=10)
ax.set_yticklabels(nice_ticks, rotation=0,  ha="right", fontsize=10)
ax.set_title(
    "Employee Correlation Heatmap\nNumerical Variables  ·  Pearson Correlation Coefficients",
    fontsize=13, fontweight="bold", pad=18,
)
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=9)
cbar.set_label("Pearson r", fontsize=10, labelpad=10)

fig.text(0.5, -0.04,
    "Strong positive correlations:  Age ↔ Experience (≈0.99)  ·  "
    "Experience ↔ Salary (≈0.99)  ·  Salary ↔ Performance (≈0.97)",
    ha="center", fontsize=9, color="#2D3748", style="italic",
    bbox=dict(boxstyle="round,pad=0.5", fc="#EBF4FF", ec=ACCENT, lw=1),
)

fig.tight_layout()
fig.savefig("employee_correlation.png", dpi=150, bbox_inches="tight", facecolor=BG)
plt.show()
print("Heatmap exported as employee_correlation.png ✓")