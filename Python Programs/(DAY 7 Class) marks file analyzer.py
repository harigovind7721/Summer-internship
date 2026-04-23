valid_marks = []
valid_count = 0
pass_count = 0
fail_count = 0

try:
    with open("marks.txt", "r") as f:
        for line in f:
            values = line.split()
            for val in values:
                try:
                    mark = int(val)
                    if mark < 0 or mark > 100:
                        raise ValueError(f"{mark} is out of range (0-100)")
                    valid_count += 1
                    if mark >= 40:
                        pass_count += 1
                    else:
                        fail_count += 1
                    valid_marks.append(mark)
                except ValueError as e:
                    if not val.lstrip('-').isdigit():
                        print(f"Invalid data skipped: '{val}'")
                    else:
                        print(f"Out of range skipped: {e}")

    print("\n--- Marks Analysis ---")
    print(f"Valid marks   : {valid_count}")
    print(f"Pass (>=40)   : {pass_count}")
    print(f"Fail (<40)    : {fail_count}")
    print(f"Marks list    : {valid_marks}")

except FileNotFoundError:
    print("Error: marks.txt file not found.")

finally:
    print("\nFile processing completed.")