# Andrew Butler             9-23-2022
# While loop demo

# swap big number for 5, peg CPU
# x = 0
# while True:
#     print(x)
#     x += 1
#     if x % 5 != 0:
#         continue
#     break



# testing that an input was correct
# x = input("Enter a float: ")
# try:
#     x = float(x)
# except:
#     print("That was not a float")


# input validation demo
num_low = 2
num_high = 10

while True:
    number = input("enter an integer: ")
    try:
        number = int(number)
    except:
        print("Please enter an integer type: {0}".format(number))
        continue
    break
    if number < num_low or number > num_high:
        print("please enter a number between {0} and {1}".format(num_low, num_high))
        continue
    break