# Andrew Butler     9-9-2022
# Lab Week 3 - Exercise 5
import math

# gathering the classes and grades from user
class1_name = input("Input Class 1: ")
class1_grade = int( input("Grade: "))
class2_name = input("Input Class 2: ")
class2_grade = int( input("Grade: "))
class3_name = input("Input Class 3: ")
class3_grade = int( input("Grade: "))
class4_name = input("Input class 4: ")
class4_grade = int( input("Grade: "))

# finding the average grade for the user
avg_grade = int((class1_grade + class2_grade + class3_grade + class4_grade)/4)

# printing result
print("The Average grade between", 
    class1_name,
    class2_name,
    class3_name, "and",
    class4_name, "is", avg_grade)