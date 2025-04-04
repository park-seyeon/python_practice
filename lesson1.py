#git status
#git add .
#git commit -m "name"
#git push

# git checkout dev 

import math
print("Hello World")
# use shortcut ctrl + ` to open/close terminal


student_count = 1000
rating = 4.99  # float
is_published = False  # Boolean T/F (case sensitive)
course = "python programming"  # string

# return number of characters
print(len(course))

# index
print(course[0])
# first character from the end of the string
print(course[-1])
# first three characters (second index not included)
print(course[0: 3])

# escape: \"
# newline: \n

first = "SeYeon"
last = "Park"
full = f"{first} {last}"
print(full)

# methods
print(course.upper())
print(course.title())
# remove white space: lstrip, rstrip, ...
print(course.strip())
# returns index
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

# numbers: integers, floats, complex numbers
print(10//3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3

print(round(2.9))
print(abs(-2.9))
# math module for math functions -- python 3 math module
print(math.ceil(2.2))

# type conversion: int(), float(), bool(), str()
x = input("x: ")
# print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

# Falsy
# ""
# 0
# None

# comparison: >, >=, <=, ==, !=, ...

# conditional statement
temperature = 25
if temperature > 30:
    print("It's warm")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# Ternary operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# logical operators: and, or, not -- short-circuit evaluation
high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# age should be between 18 and 65: chaining operator
age = 22
if 18 <= age < 65:
    print("Eligible")

# For loops
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# iterables
print(type(5))  # int
print(type(range(5)))  # range (one of complex types)

for x in "Python":
    print(x)  # string is also iterable

# lists
for x in [1, 2, 3, 4]:
    print(x)

#for item in shopping_cart:
#    print(item)

# while loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# defining function

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("SeYeon", "Park")

# types of functions 
def get_greeting(name): 
    return f"Hi {name}"

message = get_greeting("SeYeon")
file = open("content.txt", "w")
file.write (message)

# None??

# keyword arguments 
def increment(number, by): 
    return number + by

print(increment(2, by=1))

# default arguments: all optional parameters come before required parameters
def increment(number, by=1):
    return number + by 

print(increment(2)) # by default = 1
print(increment(2, 5))

# args 
def multiply(*numbers): 
    total = 1
    for number in numbers:
        total *=number 
    return total 

print(multiply(2, 3, 4, 5))