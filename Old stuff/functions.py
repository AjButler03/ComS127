# Andrew Butler             10-03-2022
# Functions demo


# print out examples
# def hello():
#     print("Hello World!")
#     print("it's a nice day out, isn't it?")
#     print("It's a long way to Friday...")
# def main():
#     hello()
#     print("The end!")


# def hello(name):
#     print("Hello " + name)
# def main():
#     hello("Alice")
#     hello("Bob")


# return value examples
# def one(a, b):
#     return a + b
# def main():
#     data1 = 5
#     data2 = 8
#     z = one(data1, data2)
#     print(z)


# def one():
#     return 10, 100
# def main():
#     z = one()
#     print(z)
#     print(z[0])

def one():
    return 10, 100
def main():
    w,z = one()
    print(w)
    print(z)

if __name__ == "__main__":
    main()