# Andrew Butler             11-16-2022
# Files exercise

def write (list):
    with open("test.txt", "w") as f:
        for i in range(0, len(list)):
            f.write(str(list[i]) +"\n")

word = ""
wordList = []
while word != "*":
    word = input("Enter a word:")
    if word != "*":
        wordList.append(word)

write(wordList)

with open("test.txt", "r") as f:
    wList = f.readlines()
wList = sorted(wList)

write(wList)