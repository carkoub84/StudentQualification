# Student Qualification Checker
# Author: Chabha Arkoub
# File Name: student_qualification.py
# Description: This app accepts student names and GPAs, then checks if the student qualifies for the Dean's List or Honor Roll.
student_first_name = ""
student_last_name = ""
gpa = float

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for any special recognition.")
