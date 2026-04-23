user_bio = """Hi, I am hari.
I love Python programming.
Improving my programming skills is my goal."""

print("Original Bio:")
print(user_bio)

cleaned_bio = user_bio.strip()

total_characters = len(cleaned_bio)
total_lines = len(cleaned_bio.split("\n"))

print("\nEach Character:")
for char in cleaned_bio:
    print(char, end=" ")

has_python = "Python" in cleaned_bio
no_java = "Java" not in cleaned_bio

updated_bio = cleaned_bio.replace("Hari", "Student")

lines_list = cleaned_bio.split("\n")

print("\n\nBio Lines List:", lines_list)
print("Updated Bio:\n" + updated_bio)
print("Total Characters: {}  |  Total Lines: {}".format(total_characters, total_lines))
print(f"Contains 'Python': {has_python}  |  'Java' not present: {no_java}")

print("\nEscape Characters:")
print("Bio analysis complete.\nThank you for using the formatter.")
print("The trainer said, \"Python string methods are very useful!\"")

print("\n========== FINAL FORMATTED OUTPUT ==========")
print("Bio Summary:")
print("Cleaned Bio     : " + cleaned_bio)
print("Total Chars     : {}".format(total_characters))
print(f"Total Lines     : {total_lines}")
print(f"Has 'Python'    : {has_python}")
print(f"No 'Java'       : {no_java}")
print("Updated Bio     : " + updated_bio)
print("=============================================")