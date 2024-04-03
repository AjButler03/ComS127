# Andrew Butler             12-05-2022
# Recursion demo

# def recur(x):
#     print("I am here:", x)
#     if x ==0:
#         return
#     recur(x-1)
# recur(5)


# challenge

rlist = []

def recursivelist(x, rlist):
    print("x is", x)
    if x == 0:
        return(rlist)
    rlist.insert(0, x)
    recursivelist(x-1, rlist)

recursivelist(5, rlist)