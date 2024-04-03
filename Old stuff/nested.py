# Andrew Butler     9-9-2022
# lecture about nested statement

x = float( input("Input a float: "))
f = False
if x > 0.0:
    f = True
    if x < 20.0:
        x = x + 5
        print("X was incremented")
        print("new value is: {0}".format(x))
else:
    x = x -5 
    print("X was decremented")
    print("new value is: {0}".format(x))
print(x,f)