import pandas as pd

student1_marks = pd.Series({"Math": 85, "Science": 78, "English": 90, "Computer": 88})

print(student1_marks)
print(student1_marks.max())
print(student1_marks.min())
print(student1_marks.sum())
print(student1_marks.mean())

marks_df = pd.DataFrame({
    "Name": ["Arun", "Binu", "Chitra"],
    "Math": [85, 70, 92],
    "Science": [78, 82, 88],
    "English": [90, 76, 95],
    "Computer": [88, 80, 91]
})

print(marks_df)

marks_df["Total"] = marks_df["Math"] + marks_df["Science"] + marks_df["English"] + marks_df["Computer"]
marks_df["Average"] = marks_df["Total"] / 4

print(marks_df)

print(marks_df.loc[marks_df["Total"].idxmax(), "Name"])

print(type(student1_marks))
print(type(marks_df))