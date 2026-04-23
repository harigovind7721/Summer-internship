student_name = "Hari"
exam_score = 68
attendance_percentage = 85
bonus_marks = 10

exam_score += bonus_marks
final_score = exam_score

score_qualified = final_score >= 75
attendance_qualified = attendance_percentage >= 80

is_eligible = score_qualified and attendance_qualified

print("====== STUDENT PERFORMANCE REPORT ======")
print(f"Student Name   : {student_name}")
print(f"Final Score    : {final_score}")
print(f"Attendance     : {attendance_percentage}%")
print(f"Score >= 75    : {score_qualified}")
print(f"Attendance >= 80: {attendance_qualified}")
print(f"Scholarship Eligible: {is_eligible}")
print("=========================================")