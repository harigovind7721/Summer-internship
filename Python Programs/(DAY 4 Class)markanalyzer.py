marks = [78, 85, 62, 90, 55]

print("===== Original List =====")
print("Marks  :", marks)
print("Length :", len(marks))

print("\n===== Accessing Elements =====")
print("First mark        :", marks[0])
print("Last mark         :", marks[-1])
print("Index 1 to 3      :", marks[1:4])


print("\n===== Updating Elements =====")
marks[2] = 70
print("After index 2 → 70      :", marks)

marks[1:4] = [88, 92]
print("After slice 1:3 → [88,92]:", marks)


print("\n===== Adding Elements =====")
marks.append(76)
print("After append(76)        :", marks)

marks.insert(1, 60)
print("After insert(1, 60)     :", marks)

marks.extend([81, 84])
print("After extend([81, 84])  :", marks)


print("\n===== Removing Elements =====")
marks.remove(55)
print("After remove(55)        :", marks)

marks.pop()
print("After pop() last element:", marks)


print("\n===== All Marks (for loop) =====")
for index, mark in enumerate(marks):
    print(f"  Index {index} : {mark}")

passed_marks = [mark for mark in marks if mark >= 60]
print("\n===== Passed Marks (>= 60) =====")
print("Passed :", passed_marks)

passed_marks.sort()
print("\n===== Sorted Ascending =====")
print(passed_marks)

passed_marks.sort(reverse=True)
print("\n===== Sorted Descending =====")
print(passed_marks)