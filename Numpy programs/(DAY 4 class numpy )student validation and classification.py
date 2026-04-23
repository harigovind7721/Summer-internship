import numpy as np
marks=np.array([35, 55, 75, 40, 90])
result=np.where(marks >= 40,'Pass','Fail')
print(result)

conditions=([marks < 40,marks < 60,marks < 80])
choices=['Fail','C','B']
final_result=np.select(conditions,choices,default='A')
print(final_result)

dup=np.array([50, 60, 50, 70, 60, 80])
unique_marks=np.unique(dup)
print(unique_marks)

has_failed=np.any(marks<40)
print("All failed",has_failed)

all_passed=np.all(marks>=40)
print("All passed",all_passed)