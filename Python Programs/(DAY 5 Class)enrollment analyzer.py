print("--------------------PART-A---------------------")
python_students={"Arun", "Meera", "Rahul", "Sneha"}
data_students={"Rahul", "Sneha", "Anu", "Vishnu"}

print("Total students enrolled for python",len(python_students))
print("Total students enrolled for python",len(data_students))
print("Student enrolled for both courses",python_students & data_students)
print("Students enrolled only in python",python_students - data_students)
print("Students enrolled only in data course",data_students-python_students)

print("-------------------PART-B-----------------------")
student_info={
    "Arun":{"age":20,"course":"python"},
    "Meera": {"age": 21, "course": "Python"},
    "Rahul": {"age": 22, "course": "Both"},
    "Sneha": {"age": 20, "course": "Both"}
}
print("Student Names\n")
for name in student_info.keys():
    print(name)

print("Student Detail\n")
for name, details in student_info.items():
   print(name, "- Age:", details["age"], ", Course:", details["course"])

student_info["Meera"]["course"] = "Data Professional Trainee"
student_info.pop("Arun")
print("\nUpdated Student Info:")
print(student_info)