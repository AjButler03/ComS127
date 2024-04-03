# Andrew Butler             10-13-2022
# Lab week 8 - exercise #3

def swap(a, b):
    temp_A = a
    temp_B = b
    b = temp_A
    a = temp_B
    return a, b
x = int(input("Enter an Integer: "))
y = int(input("Enter an Integer: "))
x, y = swap(x, y)
print(x, y)