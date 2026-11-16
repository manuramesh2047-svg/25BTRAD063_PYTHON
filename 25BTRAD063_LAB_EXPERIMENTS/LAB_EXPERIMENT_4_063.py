"""
LAB EXPERIMENT-4
NAME   : MANU R
USN    : 25BTRAD063
BRANCH : CSE - AIDE A

Run this file and choose which exercise (11, 12 or 13) to execute.
"""

import csv
import os


# ---------------------------------------------------------------------------
# Lab Exercise 11: Log file reader program
# ---------------------------------------------------------------------------
def exercise_11():
    try:
        with open("application.log", "r") as file:
            logs = file.readlines()

        error = 0
        warning = 0
        info = 0

        for line in logs:
            if "ERROR" in line:
                error += 1
            if "WARNING" in line:
                warning += 1
            if "INFO" in line:
                info += 1

        print("Log Summary")
        print("Errors:", error)
        print("Warnings:", warning)
        print("Info:", info)

        if len(logs) == 0:
            print("The log file is empty.")

    except FileNotFoundError:
        print("Log file not found.")


# ---------------------------------------------------------------------------
# Lab Exercise 12: Student data manager using files
# ---------------------------------------------------------------------------
def exercise_12():
    filename = "students.txt"

    def display_students():
        if not os.path.exists(filename):
            print("No student records found.")
            return

        with open(filename, "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
        else:
            for record in records:
                print(record.strip())

    def add_student():
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        if not roll.isdigit() or not marks.isdigit():
            print("Roll number and marks must be numeric.")
            return

        with open(filename, "a+") as file:
            file.seek(0)
            for record in file:
                if record.split(",")[0] == roll:
                    print("Roll number already exists.")
                    return

            file.write(roll + "," + name + "," + marks + "\n")

        print("Student added successfully.")

    def search_student():
        roll = input("Enter roll number to search: ")

        if not os.path.exists(filename):
            print("No student records found.")
            return

        with open(filename, "r") as file:
            for record in file:
                data = record.strip().split(",")
                if data[0] == roll:
                    print("Roll No:", data[0])
                    print("Name:", data[1])
                    print("Marks:", data[2])
                    return

        print("Student not found.")

    def update_student():
        roll = input("Enter roll number to update: ")

        if not os.path.exists(filename):
            print("No student records found.")
            return

        with open(filename, "r") as file:
            records = file.readlines()

        found = False

        for i in range(len(records)):
            data = records[i].strip().split(",")
            if data[0] == roll:
                name = input("Enter new name: ")
                marks = input("Enter new marks: ")

                if not name or not marks.isdigit():
                    print("Invalid input.")
                    return

                records[i] = roll + "," + name + "," + marks + "\n"
                found = True
                break

        if found:
            with open(filename, "w") as file:
                file.writelines(records)
            print("Student updated successfully.")
        else:
            print("Student not found.")

    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Lab Exercise 13: CSV-based payroll management system
# ---------------------------------------------------------------------------
def exercise_13():
    try:
        total_gross = 0
        total_deductions = 0
        total_net = 0
        count = 0

        with open("employees.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            print("Employee Payroll Summary")
            print("-" * 65)

            for employee in reader:
                try:
                    name = employee["Name"]
                    basic = float(employee["Basic"])
                    hra_rate = float(employee["HRA"])
                    da_rate = float(employee["DA"])
                    deduction_rate = float(employee["Deduction"])

                    if (not name.strip() or
                            min(basic, hra_rate, da_rate,
                                deduction_rate) < 0 or
                            max(hra_rate, da_rate, deduction_rate) > 100):
                        print("Invalid record:", employee)
                        continue

                    hra = basic * hra_rate / 100
                    da = basic * da_rate / 100
                    gross = basic + hra + da
                    deductions = gross * deduction_rate / 100
                    net = gross - deductions

                    print("\nEmployee:", name)
                    print("Gross Salary: Rs.", round(gross, 2))
                    print("Deductions: Rs.", round(deductions, 2))
                    print("Net Salary: Rs.", round(net, 2))

                    total_gross += gross
                    total_deductions += deductions
                    total_net += net
                    count += 1

                except (ValueError, KeyError):
                    print("Invalid employee data:", employee)

        print("\n" + "-" * 65)
        print("Total Employees:", count)
        print("Total Gross Salary: Rs.", round(total_gross, 2))
        print("Total Deductions: Rs.", round(total_deductions, 2))
        print("Total Net Salary: Rs.", round(total_net, 2))

        if count > 0:
            print("Average Net Salary: Rs.", round(total_net / count, 2))

    except FileNotFoundError:
        print("Employee CSV file not found.")


# ---------------------------------------------------------------------------
# Main selector
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Select exercise to run:")
    print("11 - Log File Reader")
    print("12 - Student Data Manager")
    print("13 - CSV Payroll Management")
    choice = input("Enter exercise number: ").strip()

    if choice == "11":
        exercise_11()
    elif choice == "12":
        exercise_12()
    elif choice == "13":
        exercise_13()
    else:
        print("Invalid exercise number!")
