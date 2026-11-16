"""
LAB EXPERIMENT-5
NAME   : MANU R
USN    : 25BTRAD063
BRANCH : CSE - AIDE A

Run this file and choose which exercise (14, 15 or 16) to execute.
"""

import random


# ---------------------------------------------------------------------------
# Lab Exercise 14: Bank account system using OOP
# ---------------------------------------------------------------------------
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance: Rs.", self.__balance)


def exercise_14():
    account = BankAccount("Arya", 5000)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using the bank system.")
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Lab Exercise 15: Library management system
# ---------------------------------------------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", self.author, "-", status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display()

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


def exercise_15():
    library = Library()

    library.add_book(Book("Python Basics", "John"))
    library.add_book(Book("Java Programming", "James"))

    while True:
        print("\n1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter book title: ")
            library.issue_book(title)
        elif choice == "3":
            title = input("Enter book title: ")
            library.return_book(title)
        elif choice == "4":
            print("Exiting library system.")
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Lab Exercise 16: Dice simulator using random module
# ---------------------------------------------------------------------------
def exercise_16():
    while True:
        print("\n1. Roll One Die")
        print("2. Roll Two Dice")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = random.randint(1, 6)
            print("Dice result:", result)
        elif choice == "2":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print("First die:", die1)
            print("Second die:", die2)
            print("Total:", die1 + die2)
        elif choice == "3":
            print("Dice simulation ended.")
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Main selector
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Select exercise to run:")
    print("14 - Bank Account System")
    print("15 - Library Management System")
    print("16 - Dice Simulator")
    choice = input("Enter exercise number: ").strip()

    if choice == "14":
        exercise_14()
    elif choice == "15":
        exercise_15()
    elif choice == "16":
        exercise_16()
    else:
        print("Invalid exercise number!")
