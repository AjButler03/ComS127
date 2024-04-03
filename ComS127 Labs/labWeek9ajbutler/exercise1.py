# Andrew Butler             10-20-2022
# Lab week 9 - exercise #1

import random

def multiples(a, b):
    numlist = []
    for i in range(a):
        numlist.append(random.randrange(a, (a+b)))
    print(numlist)
    mult_list = []
    for i in range(len(numlist)):
        if numlist[i] % b == 0:
            mult_list.append(numlist[i])
    return mult_list
        

a = int(input("Enter a positive integer: "))
b = int( input("Enter a positive integer: "))
result = multiples(a, b)
print(result)