# Andrew Butler             11-18-2022
# Matrix demo

# taking text files, convert them to integers, then adding the two list's numbers together and puting that in a seperate list.
# that third created list is then written out.

matrixA = []
matrixB = []
matrixC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for letter in ["A", "B"]:
    with open("matrix" + letter +"3x3.txt", "r") as f:
        text = f.readlines()

        for i in range (0, len(text)):
            # remove \n and white space
            text[i] = text[i].strip()
            #split each number into seperate strings
            text[i] = text[i].split()

        # convert string numbers to integers
        for i in range(0, len(text)):
            for j in range(0, len(text[i])):
                text[i][j] = int(text[i][j])
                matrixC[i][j] += text[i][j]
        if letter == "A":
            matrixA = text.copy()
        else:
            matrixB = text.copy()
print(matrixA)
print(matrixB)
print(matrixC)

# writing matrixC into it's own file
with open("matrixC3x3.text", "w") as f:
    for i in range(0, len(matrixC)):
        for j in range(0, len(matrixC[i])):
            num = str(matrixC[i][j])
            if j < len(matrixC[i]-1):
                num += " "
            f.write(num)
        if i < len(matrixC)-1:
            f.write("\n")