import numpy as np
import pandas as pd

# ── 1. Create NumPy array of marks ───────────────────────────────
marks = np.array([45, 55, 60, 70, 85])
print("Original Marks       :", marks.tolist())

# ── 2. Add 5 grace marks (vectorized — no loop) ──────────────────
marks_with_grace = marks + 5
print("After Grace (+5)     :", marks_with_grace.tolist())

# ── 3. Normalize between 0 and 1 ─────────────────────────────────
# Formula: (value - min) / (max - min)
min_val    = marks_with_grace.min()
max_val    = marks_with_grace.max()
normalized = (marks_with_grace - min_val) / (max_val - min_val)
print("Normalized (0 to 1)  :", [round(x, 4) for x in normalized.tolist()])

# ── 4. Save to CSV using np.savetxt() ────────────────────────────
np.savetxt("normalized_marks.csv", normalized, delimiter=",", fmt="%.4f")
print("\nSaved → normalized_marks.csv")

# ── 5. Load CSV back using np.genfromtxt() ───────────────────────
loaded = np.genfromtxt("normalized_marks.csv", delimiter=",")
print("Loaded from CSV      :", loaded.tolist())

# ── 6. Convert to Pandas DataFrame ───────────────────────────────
df = pd.DataFrame(loaded, columns=["Normalized Marks"])

print("\nFinal DataFrame:")
print(df)