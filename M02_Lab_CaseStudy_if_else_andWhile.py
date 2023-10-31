# Name: Dim C. Huai
# File Name: M02_Lab_CaseStudy_if_else_andWhile.py
# Description: This Python app accepts student names and GPAs and tests if the student qualifies for the Dean's List or Honor Roll.

# Initialize an empty list to store student records
student_records = []

# Define a function to check if a student qualifies for Dean's List or Honor Roll
def check_qualification(gpa):
    if gpa >= 3.5:
        return "Dean's List"
    elif gpa >= 3.25:
        return "Honor Roll"
    else:
        return "Not Qualified"

# Start accepting student records
while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    
    if last_name == 'ZZZ':
        break
    
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))
    
    qualification = check_qualification(gpa)
    
    # Print the qualification message for the student
    if qualification == "Dean's List":
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif qualification == "Honor Roll":
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for Dean's List or Honor Roll.")

    # Add the student record to the list
    student_records.append((last_name, first_name, gpa, qualification))

# Print the qualifications for each student
print("\nQualifications:")
for last_name, first_name, gpa, qualification in student_records:
    print(f"{first_name} {last_name}: GPA {gpa} - {qualification}")