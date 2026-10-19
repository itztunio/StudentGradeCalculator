
name = input("Enter your name: ")

marks = float(input("Enter your marks (0-100): "))

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n--- Student Result ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Thank you for using Student Grade Calculator!")
