import numpy as np
marks=np.array([78, 85, 62, 90, 55, 88])
print("____Total marks____\n",np.sum(marks))
print("____Avg marks_____\n",np.mean(marks))
print("____Median mark_____\n",np.median(marks))
print("____Standard deviation_____\n",np.std(marks))
print("____Minimum & Maximum_____\n",np.min(marks),
      np.max(marks))

grace_marks=marks+5
bonus_marks=marks*1.1

print("Marks after adding bonus marks\n",grace_marks)
print("Marks after adding 1.1 bonus marks\n",bonus_marks)