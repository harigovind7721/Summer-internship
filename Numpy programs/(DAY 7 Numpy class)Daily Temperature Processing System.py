import numpy as np
import sys

# ── 1. Create NumPy array of daily temperatures ───────────────────
temps_c = np.array([28, 30, 32, 35, 33])

print("=" * 50)
print("  PART 1: TEMPERATURE CONVERSION (°C → °F)")
print("=" * 50)
print(f"Celsius temperatures : {temps_c.tolist()}")

# Method 1: Python for loop
loop_result = []
for c in temps_c:
    f = (c * 9 / 5) + 32
    loop_result.append(f)
print(f"\nMethod 1 (for loop)       : {loop_result}")

# Method 2: NumPy vectorized operation (no loop)
vec_result = (temps_c * 9 / 5) + 32
print(f"Method 2 (vectorized)     : {vec_result.tolist()}")

# ── 2. Memory Usage Comparison ────────────────────────────────────
print("\n" + "=" * 50)
print("  PART 2: MEMORY USAGE")
print("=" * 50)

py_list  = [28, 30, 32, 35, 33]           # Python list
np_array = np.array([28, 30, 32, 35, 33]) # NumPy array

list_mem  = sys.getsizeof(py_list)        # sys.getsizeof() for list
array_mem = np_array.nbytes               # .nbytes for NumPy array

print(f"Python list  → sys.getsizeof() : {list_mem} bytes")
print(f"NumPy array  → .nbytes         : {array_mem} bytes")
print(f"Memory saved by NumPy          : {list_mem - array_mem} bytes")

# ── 3. Save & Load using np.save / np.load ────────────────────────
print("\n" + "=" * 50)
print("  PART 3: SAVE & LOAD FILE")
print("=" * 50)

np.save("fahrenheit_temps.npy", vec_result)
print("Saved vectorized Fahrenheit result → fahrenheit_temps.npy")

loaded_temps = np.load("fahrenheit_temps.npy")
print(f"Loaded from file : {loaded_temps.tolist()}")

print("=" * 50)
print("  All tasks completed successfully!")
print("=" * 50)