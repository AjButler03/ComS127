# Andrew Butler             10-13-2022
# Lab Week 8 - exercise #1

def multiply(a, b):
    x = 0
    if (b <= 0) and (a <=0 ):
        for i in range(a, 0):
            x-=b
    elif a <= 0:
        for i in range(b):
            x+=a
    else:
        for i in range(a):
            x+=b
    return(x)

a = int( input("Enter an integer: "))
b = int( input("Enter an integer: "))

print("The product of {0} and {1} is {2}".format(a, b, multiply(a,b)))