# Manu R
# 25BTRAD063
# Python Programming
# Lab Experiment - 1

# =====================================================
# Lab Exercise 1: Installing Python, Setting up VS Code / PyCharm, Jupyter Notebook
# =====================================================
# Steps to install Python:
# 1. Go to the official Python website and download the latest version.
# 2. Run the installer.
# 3. Select "Add Python to PATH" before clicking Install.
# 4. Click "Install Now".
# 5. Open Command Prompt and type: python --version
# 6. If the version number appears, Python is installed successfully.


# =====================================================
# Lab Exercise 2: Write and execute a basic Python program
# =====================================================
print("--- Lab Exercise 2 ---")

# Program 1
name = "Manu"
print("My name is", name)

# Program 2
a = 10
b = 20
sum = a + b
print("First number:", a)
print("Second number:", b)
print("Sum:", sum)


# =====================================================
# Lab Exercise 3: Programs using variables, operators, and input/output
# =====================================================
print("\n--- Lab Exercise 3 ---")

# Program 1: Sum and product
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("Product =", a * b)

# Program 2: Simple interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)


# =====================================================
# Lab Exercise 4: Simple calculator and area calculation programs
# =====================================================
print("\n--- Lab Exercise 4 ---")

# Program 1: Simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

# Program 2: Area of a circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle =", area)
