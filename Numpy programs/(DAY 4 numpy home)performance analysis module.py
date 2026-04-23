import numpy as np


scores = np.array([25, 45, 65, 85, 95])
tags = np.where(scores < 40, "Poor", "Good")
print("Task 1 - Tags:", tags)


conditions = [scores < 40, scores < 70, scores < 90]
choices    = ["Poor", "Average", "Good"]
cats = np.select(conditions, choices, default="Excellent")
print("Task 2 - Categories:", cats)


course_ids = np.array([101, 102, 101, 103, 102, 104])
unique_ids = np.unique(course_ids)
print("Task 3 - Unique IDs:", unique_ids)


high_scorer = np.any(scores > 90)
print("Task 4 - Any high scorer?:", high_scorer)


above_min = np.all(scores > 30)
print("Task 5 - All above 30?:", above_min)