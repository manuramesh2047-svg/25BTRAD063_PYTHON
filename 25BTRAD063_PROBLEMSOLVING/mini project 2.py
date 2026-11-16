"""
MINI PROJECT - 2
Name : MANU R
USN  : 25BTRAD063
Dept : AIDE-A

Program 1: OTP Generator
Program 2: Student Grading Automation
"""

# =====================================================================
# PROGRAM 1: OTP GENERATOR
# =====================================================================
import random


def otp_generator():
    otp = random.randint(100000, 999999)
    print("Your OTP is:", otp)

    user_otp = int(input("Enter the OTP: "))

    if user_otp == otp:
        print("OTP Verified Successfully!")
    else:
        print("Invalid OTP!")


# =====================================================================
# PROGRAM 2: STUDENT GRADING AUTOMATION
# =====================================================================
def student_grading():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 40:
        grade = "E"
    else:
        grade = "F"

    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)

    if marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


# =====================================================================
# MAIN
# =====================================================================
if __name__ == "__main__":
    print("Name : MANU R")
    print("USN  : 25BTRAD063\n")

    print("=" * 40)
    print("OTP GENERATOR")
    print("=" * 40)
    otp_generator()

    print("\n" + "=" * 40)
    print("STUDENT GRADING AUTOMATION")
    print("=" * 40)
    student_grading()
