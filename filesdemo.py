# Andrew Butler             11-16-2022
# Files Demo


# writing demo
writeFile = open("test.txt", "w")
writeFile.write("3")
writeFile.close()

# reading demo
readFile = open("test.txt", "r")
text = readFile.read()
readFile.close()
print(text)

# append demo
appendFile = open("test.txt", "a")
appendFile.write("\n This is the next line")
print("File name?:", appendFile.name)
print("Is the file closed?", appendFile.closed)
print("What is the file mode?:", appendFile.mode)
appendFile.close()

print()
print("File name?:", appendFile.name)
print("Is the file closed?", appendFile.closed)
print("What is the file mode?:", appendFile.mode)



# writing demo pt2
# note: this was a Wednesday lecture
# with open("test.txt", "w") as f:
#     f.write("Taco Tuesday (on Wednesday)\n")

# # reading demo pt2
# with open("Test.txt", "r") as f:
#     text = f.read()
# print(text)

# # appending demo pt2
# with open("test.txt", "a") as f:
#     f.write("Thanksgiving Break!")
