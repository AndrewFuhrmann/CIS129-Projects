# Andrew Fuhrmann
# CIS129
# Lab 11

import csv # Import the csv module to handle CSV files

# Function to write grades to a plain text file (grades.txt)
def write_grades_to_txt():
    grade_input = ''
    with open('grades.txt', 'w') as file:
        print("Enter grades one by one. Type 'done' to finish.")
        while grade_input.lower() != 'done':
            grade_input = input("Enter grade (or 'done' to finish): ")
            if grade_input.lower() != 'done':
                try:
                    grade = float(grade_input)
                    file.write(f"{grade}\n")
                except ValueError:
                    print("Invalid input. Please enter a numeric grade or 'done'.")

# Function to read grades from grades.txt and calculate total, count, average
def read_grades_from_txt():
    try:
        with open('grades.txt', 'r') as file:
            grades = []
            for line in file:
                grade = float(line.strip())
                grades.append(grade)
                print(f"Read grade: {grade}")
        total = sum(grades)
        count = len(grades)
        average = total / count if count != 0 else 0
        print(f"\nTotal of grades: {total}")
        print(f"Number of grades: {count}")
        print(f"Average grade: {average:.2f}")
    except FileNotFoundError:
        print("grades.txt file not found. Please run the writing option first.")

# Function to write student records (name + 3 exam grades) to grades.csv
def write_student_records_to_csv():
    first_name = ''
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        print("Enter student records. Type 'done' as first name to finish.")
        while first_name.lower() != 'done':
            first_name = input("Enter first name (or 'done' to finish): ")
            if first_name.lower() != 'done':
                last_name = input("Enter last name: ")
                try:
                    exam1 = int(input("Enter Exam 1 grade: "))
                    exam2 = int(input("Enter Exam 2 grade: "))
                    exam3 = int(input("Enter Exam 3 grade: "))
                    writer.writerow([first_name, last_name, exam1, exam2, exam3])
                except ValueError:
                    print("Invalid input. Please enter integer grades.")

# Main function to display menu and handle user choices
def main():
    choice = ''
    while choice != '4':
        print("\nWhat would you like to do?")
        print("1 - Write grades to grades.txt")
        print("2 - Read grades from grades.txt")
        print("3 - Write student records to grades.csv")
        print("4 - Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            write_grades_to_txt()
        elif choice == '2':
            read_grades_from_txt()
        elif choice == '3':
            write_student_records_to_csv()
        elif choice == '4':
            print("Goodbye!")  # Exit message
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
