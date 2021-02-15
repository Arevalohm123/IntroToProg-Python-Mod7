# _______________________________________________________#
# Assignment #7
# Dev: Andrei Arevalo
# Date: February 14, 2021
# ChangeLog:
# AArevalo, 2/14/2021, Initial Revision
# _______________________________________________________#

# Assignment Task: Create a program that demonstrates how
#   Pickling and Structured error handling work
# _______________________________________________________#

# Exception Handling in Python
# Definition: Exception - An error detected during execution of
#   a sequence of code. There are different types of exceptions,
#   for example dividing by zero ("ZeroDivisionError"), naming errors
#   ("NameError"), type error ("TypeError")
# Source - https://docs.python.org/3/tutorial/errors.html

import pickle


# EXAMPLE 1
def this_fails():
    y = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print("Handling run-time error:", err)

# EXAMPLE 2
while True:
    try:
        x = int(input("Please enter a number: "))
        print("Yay! You entered a number and it was", x)
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

# Pickling in Python
# Definition: Pickling - The "pickle" module within Python is used
#   for serializing and de-serializing python object structures. This
#   is useful in scenarios where you want to transfer data from one
#   system to another and then store it in a file or database.
# Source - https://www.tutorialspoint.com/python-pickling


# EXAMPLE 3
lst = ["Snow", "Carrot", "Buttons", "Coal"]

# Pickle a List
with open("datafile.txt", "wb") as xy:
    pickle.dump(lst, xy)
    print("\nThe list has been pickled!")

pickle_off = open("datafile.txt", "rb")
import_list = pickle.load(pickle_off)
print("\nThe list has been un-pickled!")
print("\n", import_list)

