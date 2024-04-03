# <Andrew J. Butler>                    <08/25/2022>
# Lecture 3

"""
this is a multi-line comment
it has multiple lines in it
"""
'''
This is also a multi-line comment
it also has multiple lines
'''
#these are string ending examples
print("Hello World!")
print("Hello World!", end="")
print("Hello World!", end="   ABC")
print("Hello World!", end="\n\n\n")

#these are escape character examples
print("this is a \nnew line")
print("this is a \ttab character")
print("this is a \\ slash")
print("this is a \ slash")
#the double slash is in case you want something after the second slash; without two you just don't end up with anything
print('this is a single quote \' it is really neat')
print("this is a double quote \" it is really neat")
print()


#input examples
name = input("What is your name?: ")
print("well, hello there", name, " it's a nice day isn't it?")
print("Hello " + name + "!")