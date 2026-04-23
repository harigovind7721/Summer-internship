n = int(input("Enter number of students: "))

total_valid = 0
passed = 0
failed = 0

for i in range(n):
    mark = int(input(f"Enter mark for student {i + 1} (-1 to stop): "))

    if mark == -1:
        break

    if mark < 0 or mark > 100:
        print("Invalid mark, skipped")
        continue

    total_valid += 1

    if mark >= 80:
        print(f"Student {i + 1}: Excellent")
        passed += 1
    elif mark >= 60:
        print(f"Student {i + 1}: Good")
        passed += 1
    elif mark >= 40:
        print(f"Student {i + 1}: Pass")
        passed += 1
    else:
        print(f"Student {i + 1}: Fail")
        failed += 1
else:
    print("Analysis completed successfully")

print(f"Total valid students: {total_valid}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")