import csv
import os

FILE_NAME = "students.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Name",
            "RollNo",
            "Tamil",
            "English",
            "Maths",
            "Total",
            "Percentage",
            "Grade"
        ])

def calculate_grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 50:
        return "C"
    else:
        return "Fail"

def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")

    tamil = int(input("Tamil Mark: "))
    english = int(input("English Mark: "))
    maths = int(input("Maths Mark: "))

    total = tamil + english + maths
    percentage = round((total / 300) * 100, 2)

    grade = calculate_grade(percentage)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            name,
            roll_no,
            tamil,
            english,
            maths,
            total,
            percentage,
            grade
        ])

    print("\n Student Added Successfully!")

def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n--- STUDENT RECORDS ---")
        for row in reader:
            print(row)

def search_student():
    roll = input("Enter Roll Number: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 1 and row[1] == roll:
                print("\nStudent Found:")
                print(row)
                found = True
                break

    if not found:
        print(" Student Not Found")

def show_topper():
    topper_name = ""
    highest_total = -1

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            total = int(row[5])

            if total > highest_total:
                highest_total = total
                topper_name = row[0]

    if highest_total != -1:
        print("\n TOPPER STUDENT")
        print("Name :", topper_name)
        print("Total Marks :", highest_total)
    else:
        print("No Records Found")

while True:

    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Show Topper")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        show_topper()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
