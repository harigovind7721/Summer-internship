import numpy as np


rand_scores = np.random.rand(5)
randn_scores = np.random.randn(5)
print("rand():", rand_scores)
print("randn():", randn_scores)


marks = np.random.randint(35, 101, size=(3, 4))
print("\nMarks Table:\n", marks)


ids = [101, 102, 103, 104, 105]
selected = np.random.choice(ids, size=2, replace=False)
print("\nSelected Students:", selected)

np.random.seed(10)
fixed = np.random.rand(3)
print("\nSeeded Output:", fixed)

arr = np.array([10, 20, 30, 40, 50, 60])
print("\n3rd element:", arr[2])
print("Index 1 to 4:", arr[1:5])
print("Last element:", arr[-1])
print("Every 2nd:", arr[::2])
print("Reversed:", arr[::-1])