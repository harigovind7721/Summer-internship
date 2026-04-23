import numpy as np

marks_term1 = np.array([60, 70, 80, 90])
marks_term2 = np.array([65, 75, 85, 95])
total      = marks_term1 + marks_term2
difference = marks_term2 - marks_term1
increased  = total * 1.05
print("Total:", total)
print("Difference:", difference)
print("5% Increase:", increased)

print("Marks > 150:", total[total > 150])
print("Between 140–170:", total[(total >= 140) & (total <= 170)])

print("Sum:", np.sum(total))
print("Mean:", np.mean(total))
print("Max:", np.max(total))
print("Min:", np.min(total))
print("Std Dev:", np.std(total))


marks2d = np.array([[70, 80, 90], [60, 75, 85]])
print("Column-wise sum:", np.sum(marks2d, axis=0))
print("Row-wise mean:", np.mean(marks2d, axis=1))

arr = np.array([1, 2, 3, 4, 5, 6])
print("Shape:", arr.shape, "| ndim:", arr.ndim, "| size:", arr.size, "| dtype:", arr.dtype)
reshaped = arr.reshape(2, 3)
print("Reshaped:\n", reshaped)
print("Ravelled:", reshaped.ravel())