# Andrew Butler             9-15-2022
# Lab Week 4 - Python Conditional Results


# Question 1
print("Question 1")
print()

print("What I got by hand: False, will print \"Computer's Answer: False\"")
x = 7
y = 12

if x*x*x + y == y * x + 47:
    print("Computer Answer: True")
else:
    print("Computer's Answer: False")

print(" x * x * x + y = {0}".format(x * x * x + y))
print("y * x + 47 = {0}".format(y * x + 47))
print()

# Question 2
print("Question 2")
print()

print("What I got by hand: True, will print \"Computer's Answer: True\"")
x = 3
y = 4
z = 5

if 1000*x / y / z + 2 <= x ** 2 * 20:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")

print("1000 * x / y / z + 2 = {0}".format(1000 * x / y / z + 2))
print("x ** 2 * 20 = {0}".format(x ** 2 * 20))
print()

# Question 3
print("Question 3")
print()

print("What I got by hand: True, will print \"Computer's Answer: True\"")
x = 12
y = 47
z = 3

if x + y // z >= x * z % y + 2:
    print("Computer's Answer: False")
else:
    print("Computer's Answer: False")

print("x + y // z = {0}".format(x + y // z))
print("x * z % y + 2 = {0}".format(x * z % y + 2))
print()

# Question 4
print("Question 4")
print()

print("What I got by hand: False, will print \"Computer's Answer: False\"")
x = 8
y = 9
z = 10

if x * y % z != z % y * x:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")

print("x * y % z = {0}".format(x * y % z))
print("z % y * x = {0}".format(z % y * x))
print()

# Question 5
print("Question 5")
print()

print("What I got by hand: y = 44, z = 6. Result is False, will print \"Computer's Answer: False\"")
x = 3
y = x + 400 // 3 ** 2
z = x * y % 10 + 2 ** 2

if z * y ** 2 % 5 == z * 2 ** y % 4:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")
print("z * y ** 2 % 5 = {0}".format(z * y ** 2 % 5))
print("z * 2 ** y % 4 = {0}".format(z * 2 ** y % 4))
print()