# Andrew Butler             11-4-2022
# Try / except demo

# print("This variable is not defined yet: ", x)

# nums = [10,20,30,40]
# print(nums[40])

# try:
#     print("This variable is not defined yet: ", x)
# except:
#     print("The variable does not exist yet")
# print("Code continues")

# try:
#     num = [10,20,30,40]
#     print(num[40])
# except:
#     print("The index is not valid")
# print("Code continues")

# newX = input("Enter a string: ")
# try:
#     newX = float(newX)
# except:
#     print("you must enter a float")
# print("The code continues")

# try:
#     items = ['a', 'b']
#     third= items[2]
#     print("This won'd do")
# except Exception as e:
#     print("error: ", e)
# print("Code continues")


# myList = ["Pizza", "Steak", "Pineapple", "Tacos", "Ravioli"]
# try:
#     average = sum(myList) / len(myList)
# except Exception as e:
#     print("Error: ", e)

# if len(myList) > 0:
#     average = sum(myList) / len(myList)
# else:
#     average = 0

# myList = ["Pizza", "Steak", "Pineapple", "Tacos", "Ravioli"]
# index = 3
# if 0 <= index < len(myList):
#     print(myList[index])
# else:
#     print("Index out of range")

# myDict = {"Adventure" : "Percy Jackson", "Horror" : "IT", "Graphics" : "Spider-Man"}
# key = "Sci-Fi"
# if key in myDict.keys():
#     value = myDict[key]
#     print(value)
# else:
#     print("Key not in dictionary")

# try, except, else, finally
def divide(x, y):
    value = None
    try:
        value = x/y
    except Exception as e:
        print("Error: ", e)
    else:
        print("The answer is", value)
    finally:
        print("This will always print, exception or no")
    return value
value1 = divide(10, 2)
value2 = divide(20, 0)
print(value1, value2)