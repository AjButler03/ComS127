# Andrew Butler             10-13-2022
# Lab week 8 - exercise #2

def sortorder(a, b, c):
    tup = ()
    if a <= b <= c:
        tup = (a, b, c)
    elif a <= c <= b:
        tup = (a, c, b)
    elif c <= a <= b:
        tup = (c, a, b)
    elif c <= b <= a:
        tup = (c, b, a)
    elif b <= a <= c:
        tup = (b, a, c)
    elif b <= c <= a:
        tup = (b, c, a)
    else:
        print("Error")
    return(tup)

a = int( input("Enter an integer: "))
b = int( input("Enter an integer: "))
c = int( input("Enter an integer: "))
print("The sorted values are: {0}".format(sortorder(a, b, c)))

# ABC
# ACB
# CAB
# CBA
# BAC
# BCA