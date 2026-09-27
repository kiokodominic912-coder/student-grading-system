again = "yes"
student_count = 0
total_marks = 0
highest_marks = 0
lowest_marks = 100

while again == "yes":

    print("STUDENT GRADING SYSTEM")

    name = input("Enter student's name: ")
    student_count = student_count + 1

    marks = int(input("Enter student's marks: "))
    if marks > highest_marks:
        highest_marks = marks

    if marks > lowest_marks:
        lowest_marks = marks
    total_marks = total_marks + marks

    print("Student:", name)
    print("Marks:", marks)

    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    if marks >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    print("Grade:", grade)
    print("Result:", result)

    again = input("Do you want to enter another student? (yes/no): ")
print("total students:", student_count)
average = total_marks / student_count
print("Average:", average)
print("highest marks:", highest_marks)
print("lowest marks:", lowest_marks)


