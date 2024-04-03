# Andrew Butler             9-29-2022
# Lab week 6 - Exercise #1

counter = int( input("Enter an integer: "))

while counter > 0:
    if counter % 2 == 0:
        print(counter)
        counter -= 2
    else:
        counter -=1