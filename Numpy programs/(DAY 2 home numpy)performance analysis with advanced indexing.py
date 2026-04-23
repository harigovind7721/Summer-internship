import numpy as np
import numpy as np

attendance = np.random.rand(10)
print("All values:", attendance)
present = attendance[attendance > 0.5]
print("Present:", present)


scores = np.random.randint(0, 101, size=15)
print("All scores:", scores)
print("Scores > 60:", scores[scores > 60])
print("Divisible by 5:", scores[scores % 5 == 0])


arr = np.array([100, 200, 300, 400, 500])
print("Selected:", arr[[0, 2, 4]])


mat = np.random.randint(1, 51, size=(4, 4))
print("Matrix:\n", mat)
print("2nd row:", mat[1])
print("3rd column:", mat[:, 2])

uni  = np.random.uniform(0, 1, size=5)
norm = np.random.normal(0, 1, size=5)
print("Uniform:", uni)
print("Normal:", norm)