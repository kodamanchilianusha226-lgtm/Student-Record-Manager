import re

# File name
FILE_NAME = "students.txt"


# Validate Email using Regex
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# Add Student
def add_student():
    try:
        name = input("Enter Student Name: ")
        roll_no = input("Enter Roll Number: ")
        email = input("Enter Email: ")

        # Check empty input
        if name == "" or roll_no == "" or email == "":
            raise ValueError("All fields are required!")

        # Validate email
        if not validate_email(email):
            raise ValueError("Invalid Email Address!")

        # Save student data to file
        with open(FILE_NAME, "a") as file:
            file.write(name + "," + roll_no + "," + email + "\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Something went wrong:", e)


# Read Student Data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
                return

            print("\nStudent Records:")
            print("----------------")

            for line in data:
                name, roll_no, email = line.strip().split(",")
                print("Name:", name)
                print("Roll Number:", roll_no)
                print("Email:", email)
                print("----------------")

    except FileNotFoundError:
        print("No student file found. Add a student first.")

    except Exception as e:
        print("Error:", e)


# Main Program
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Read Student Data")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            read_students()

        elif choice == 3:
            print("Program exited.")
            break

        else:
            print("Invalid choice! Enter 1, 2 or 3.")

    except ValueError:
        print("Invalid input! Please enter a number.")