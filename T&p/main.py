# Variables

name = "Tony Stark"
age = 51
is_genius = True

print("name: " , name)
print("age: " , age)
print("is_genius: " , is_genius)

# Input

superhero = input("Enter Superhero name: ")
print("Superhero: " , superhero)

# Type conversions

old_age = input("Enter old age: ")
new_age = int(old_age) + 2
print(new_age)

# Concatination 

first =  input("Enter first number: ")
second = input("Enter second number: ")

sum = int(first) + int(second)
print("sum: " + str(sum))

# String operations

name = "Tony Stark"
print("name: " , name)
print("name in lower case :", name.lower())
print("name in upper case :", name.upper())

print("S find at ", name.find('S'))

print("Name is replace with",name.replace("Tony Stark", "Iron Man"))
print("T" in name)


# Artihmatic operators

num1 = 10
num2 = 5

print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Divide:", num1/num2)
print("Excat value in divide:", num1//num2)
print("Reminder:", num1%num2)
print("Power:", num1**num2)

#Shothands to write operations
# i = 5
# i = i + 2
# i += 2
# i -= 2
# i *= 2

# Comparison operators
print(3 > 2)
print(3 < 2)
print(3 <= 2)
print(3 >= 2)
print(3 == 2)
print(3 != 2)

# Logical operators

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(not 2>3)

# if else conditions

num = 10
if num > 5:
    print("Number is greater than 5")
else:
    print("Number is less than or equal to 5")
    
age = 19
if age >= 18:
    print("Major")
    print("Eligible for voting")
elif age < 18 and age > 3:
    print("Minor")
    print("Not eligible for voting")
else:
    print("Child")
    print("You're a school going student")

# Range

numbers = range(5)
print(numbers)

# Loop

for i in range(1, 11):
    print(i)
    
i = 1
while i < 10:
    print(i * '*')
    i += 1
    
i = 10
while i > 1:
    print(i * '*')
    i -= 1
    
    
# List

marks = [95, 98, 97]
print(marks)

print(marks[0])
print(marks[1])
print(marks[-1])

print(marks[0 : 2]) # 2 is excluded

for score in marks:
    print(score)
    
marks.append(100)
marks.insert(0, 99)
print(marks)

i = 0
while i < len(marks):
    print(marks[i])
    i += 1
    
marks.clear()
print(marks)

# Break and continue
students = ["ram", "shyam", "Radhika", "Sourabh"]

for student in students:
    if student == "Radhika":
        break
    print(student)
    
# Tuples (immutable)
marks = (95, 10, 56, 56, 45)
print(marks.count(56))
print(marks.index(10))

# Set
marks = {89, 90, 56, 78, 78}
for score in marks:
    print(score)
    
# Dictionary
marks = {"eng": 89, "chem": 90}
print(marks["chem"])
marks["Phy"] = 90

print(marks)

# functions

# inbuilt function
# module function

from math import sqrt
print(sqrt(5))
 
# user defined function

def print_sum(first, second):
    print(first+second)

print_sum(1, 2)