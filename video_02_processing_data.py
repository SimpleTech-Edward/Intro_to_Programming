"""
RUNNING A PYTHON FILE
We are using pythonanywhere.com, it has a free tier, you can use repl.it as well. 

PRINT FUNCTION
A function we use to display data on the terminal

MATH OPERATIONS
All the standard math operations are available and follow the PEMDAS rule

REASSIGNING VARIABLES
Updating variables by performing math operations
Reassigning variables to different data types are possible in Python


FUNCTIONS THAT HELP IDENTIFY DATA TYPES
We can use two functions to help understand what data types exist,
"""
greeting = "hello world"
print(greeting)
print("hello world")

number = 42
number = number + 1
print(number)

number = 4 * 2
number = 4 - 2
number = 4 / 2
number = 4 // 2

# CHECKING FOR DATA TYPES
print(type("hello"))
print(isinstance("hello", str))