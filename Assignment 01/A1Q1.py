def get_grade(marks):
    if marks >= 80: return "A+", 4.00
    elif marks >= 75: return "A", 3.75
    elif marks >= 70: return "A-", 3.50
    elif marks >= 65: return "B+", 3.25
    elif marks >= 60: return "B", 3.00
    elif marks >= 55: return "B-", 2.75
    elif marks >= 50: return "C+", 2.50
    elif marks >= 45: return "C", 2.25
    elif marks >= 40: return "D", 2.00
    else: return "F", 0.00

# Get input from user
first_incourse = float(input("Enter first incourse marks: "))
second_incourse = float(input("Enter second incourse marks: "))
attendance = float(input("Enter attendance marks: "))
final = float(input("Enter final marks: "))

# Calculate total
total = ((first_incourse + second_incourse) / 2) + attendance + final

# Get grade
letter_grade, grade_point = get_grade(total)

# Print result
print("\nRoll | Letter Grade | Grade Point")
print("-" * 35)
print(f"80   | {letter_grade:^11s} | {grade_point:^10.2f}")