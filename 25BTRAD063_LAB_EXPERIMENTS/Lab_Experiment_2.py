# NAME : MANU R
# USN  : 25BTRAD063
# DEPT : AIDE-A
# LAB EXPERIMENTS - 2

# =====================================================
# Lab Exercise 5 - Number Guessing Game
# =====================================================
import random

print("--- Lab Exercise 5: Number Guessing Game ---")
number = random.randint(1, 100)
print("Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break


# =====================================================
# Lab Exercise 6 - Prime Number and Factorial
# =====================================================
print("\n--- Lab Exercise 6: Prime Number and Factorial ---")

# Prime Number Program
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

# Factorial Program
n = int(input("\nEnter a number to find factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial of", n, "is", factorial)


# =====================================================
# Lab Exercise 7 - Fibonacci Series Using Recursion
# =====================================================
print("\n--- Lab Exercise 7: Fibonacci Series Using Recursion ---")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()
