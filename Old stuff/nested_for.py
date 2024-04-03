# Andrew Butler             9-28-2022
# Nested for loops

# numA = int( input("Enter an integer: "))
# numB = int( input("Enter an integer: "))
# numC = int( input("Enter an integer: "))
# numD = int( input("Enter an integer: "))
# for i in range(0, numA):
#     for j in range(0, numB):
#         for k in range(0, numC):
#             for m in range(0, numD):
#                 print("i = {0}, j = {1}, k = {2}, m = {3}".format(i, j, k, m))



# x = int( input("Enter width: "))
# y = int( input("Enter height: "))
# for i in range(0, y):
#     for k in range(0, x):
#         print("*", end="")
#     print()


# num_low = 1
# num_high = 11
# for i in range(num_low, num_high):
#     for j in range(num_low, num_high):
#         print("{0} x {1} = {2}".format(i, j, (i*j)))
#     print()


for i in range(0, 3):
    password = input("Enter password: ")
    if password == "secret":
        print("correct login")
        break
else:
    print("You have entered the wrong password 3 times")