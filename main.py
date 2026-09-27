# Simple Student Result Processor
# BIT223 - Week 2 Mini-Project
# Procedural Python Version

def calculate_average(marks):
    """Calculate the average of a student's marks."""
    return sum(marks) / len(marks)


def classify_result(average):
    """Classify a student's result using the average mark."""
    if average >= 70:
        return "Distinction"
    elif average >= 60:
        return "Credit"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"


def get_mark(subject):
    """Read and validate a mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter {subject} mark (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter a mark between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def display_student_result(student):
    """Display the calculated result for one student."""
    average = calculate_average(student["marks"])
    classification = classify_result(average)

    print("\n--- Student Result ---")
    print(f"Name: {student['name']}")
    print(f"Registration Number: {student['registration_number']}")
    print(f"Marks: {student['marks']}")
    print(f"Average: {average:.2f}")
    print(f"Classification: {classification}")


def process_students():
    """Collect and process results for multiple students."""
    students = []

    print("===================================")
    print("   SIMPLE STUDENT RESULT PROCESSOR")
    print("===================================")

    try:
        number_of_students = int(input("Enter number of students: "))
        if number_of_students <= 0:
            print("Number of students must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid whole number.")
        return

    for student_number in range(1, number_of_students + 1):
        print(f"\nEntering details for Student {student_number}")

        name = input("Enter student name: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input("Enter student name: ").strip()

        registration_number = input("Enter registration number: ").strip()
        while not registration_number:
            print("Registration number cannot be empty.")
            registration_number = input("Enter registration number: ").strip()

        print("Enter marks for three subjects:")
        marks = [
            get_mark("Subject 1"),
            get_mark("Subject 2"),
            get_mark("Subject 3"),
        ]

        student = {
            "name": name,
            "registration_number": registration_number,
            "marks": marks
        }

        students.append(student)

    print("\n\n===================================")
    print("           ALL RESULTS")
    print("===================================")

    for student in students:
        display_student_result(student)

    print("\nProcessing complete.")


if __name__ == "__main__":
    process_students()
