# Andrew Butler             Various dates
# This is a test document, mostly to test things away from actual documents. Digital scratch paper, if you will.

# name = input("Enter Your Name: ")
# num = int( input("Enter an integer: "))
# # unfortunately, it looks like you can't use "+" to implement a number into a printed string.
# # It doesn't seem to like it.
# print("Greetings, " + name + ". The number you entered is", num, ".")
import math

# name = "Andrew"
# sport = "Baseball"
# print(f"{name} likes {sport}.")

# firstname = "Andrew"
# lastname = "Butler"
# third = "test"
# print(" first: {0} last: {1} third: {2}".format(firstname, lastname, third))

# 9/14/2022
# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# num3 = int(input("Num3: "))
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# elif num3 > num1 and num3 > num2:
#     print(num3)
# else:
#     print("There isn't one number that is larger than the other two.")

# 9-15-22
#print(101 // 4)
# print(105553116266496 % 4)

# 9-23-22
# x = 0
# while x <= 10000:
#     print(x)
#     x += 1


# 9-30-2022
# num_numbers = int( input("How many numbers are being averaged: "))
# counter = 0
# sumation = 0
# while counter < num_numbers:
#     sumation += float(input("Enter a number: "))
#     counter += 1
# print("The average is {0}".format(sumation/num_numbers))

# n_asterisks = int( input("Enter an integer: "))
# counter = 0
# for i in range(0, n_asterisks):
#     for j in range(0, n_asterisks):
#         if j == counter:
#             print("*", end="")
#         else:
#             print(".", end="")
#     counter += 1
#     print()

# 10-02-2022
# for i in range(-1, 5):
#     print(i)

# 10-20-2022
# function to find minimum and maximum position in list
# def minimum(a, n):
 
#     # inbuilt function to find the position of minimum
#     minpos = a.index(min(a))
 
#     # inbuilt function to find the position of maximum
#     maxpos = a.index(max(a))
 
#     # printing the position
#     print("The maximum is at position", maxpos + 1)
#     print("The minimum is at position", minpos + 1)
# # driver code
# a = [3, 4, 1, 3, 4, 5]
# minimum(a, len(a))
# list = [5.0, 0.0]
# print(min(list))




# 11-1-2022
# UltimateTODO.py testbed, so this is fairly lengthy. Could've probably done it on the file itself, but this is what I thought of first so this is what I'm doing. 
testlist = {"One":["1", "2", "3"], "Two": ["4", "5", "6"], "Three": ["7", "8", "9"]}
item = "10"
# def checkItem(item, todoList):
#     itemFound = False
#     keyName = ""
#     index = -1
#     for key in todoList:
#         if item in todoList[key]:
#             keyName = key
#             index = todoList[key].index(item)
#             itemFound = True
#     return itemFound, keyName, index
# def addItem(item, toList, todoList):
#     item_in_list, keyName, index = checkItem(item, todoList)
#     if item_in_list == False:
#         todoList[toList].append(item)
#     else:
#         print("Item {0} already in list {1} at index {2}".format(item, keyName, index))
#     return todoList
# def deleteItem(item, todoList):
#     itemFound, keyName, index = checkItem(item, todoList)
#     if itemFound == True:
#         del todoList[keyName][index]
#     else:
#         print("Error: item {0} is not in the todo list".format(item))
#     return itemFound, todoList
# def moveItem(item, toList, todoList):
#     itemFound, todoList = deleteItem(item, todoList)
#     if itemFound == True:
#        todoList = addItem(item, toList, todoList)  
#     return todoList
# def printTODOList(todoList):
#     for key in todoList:
#         print(key + ": ", end = "")
#         print(todoList[key])

# 11-7-2022
# num = 665555
# numstr = str(num)
# numodds = 0
# for i in range(0, len(numstr)):
#     if int(numstr[i]) % 2 != 0:
#         numodds += 1
# print(numodds)