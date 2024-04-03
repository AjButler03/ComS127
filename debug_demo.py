# Andrew Butler             10-31-2022
# Debugger demo

def fnDivideNumber(n):
    n/=2
    print(n)
    return n

def fnPrintNumber(n):
    print(n)

def main():
    number = int( input("Enter a number: "))
    fnPrintNumber(number)

    newNumber = fnDivideNumber(number)
    print(newNumber)

if __name__ == "__main__":
    main()

# right click on left to add red dot; breakpoint
# f5 to run debugger

# def fnDouble(x):
#     for i in range(0, 1000):
#         x *= 2
#     return x

# num = 5
# den = 1

# for i in range(0, 4):
#     print(("Hi {0}!".format(i)))

# fnDouble(5)

# print(den)
# total = num / den

# print(total)