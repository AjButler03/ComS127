# Andrew Butler             10-19-2022
# Strings demo

# animal = input("Enter an animal: ")
# while True:
#     index = int(input("Enter an integer: "))
#     if index >= len(animal) or index < 0:
#         print("bad number numnuts")
#     else:
#         break
# letter = animal[index]
# print(letter)

# car = input("Enter a type of car: ")
# index = 0
# while index < len(car):
#     print(car[index])
#     index+=1

# car = input("Enter a type of car: ")
# for letter in car:
#     print(letter)

# count = 0
# clothes = input("enter a clothing company: ")
# searchletter = input("Enter a letter to search for: ")
# for letter in clothes:
#     if letter == searchletter:
#         count += 1
# print(count)

# s = "Monty Python"
# print(s[0:3])
# print(s[1:4])
# print(s[6:250])
# print(s[:])

# word = "banana"
# j = -1
# for i in range(len(word)):
#     print(word[j], end="")
#     j -= 1
# print() # alternate way
# print(word[::-1])


# fruit = "banana"
# if "n" in fruit:
#     print("There is the letter N in fruit")

# fruit = input("Enter a fruit: ")
# letter = input(("Enter a letter: "))
# count = 0
# for i in range (fruit):
#     if letter in fruit:
#         count+=1
# print(count)



# 10-21-2022
# strings demo conclusion

# def lastname_in_name(name, lastname):
#     if lastname in name:
#         print(lastname + " is in the name " + name)
# def main():
#     lastname_in_name("John Smith", "Smith")
# if __name__ == "__main__":
#     main()

# make a function which takes a string as input and returns that string in all uppercase
# def uppercase(string):
#     modifiedstring = string.upper()
#     return modifiedstring
# def main():
#     string = input("Enter a string: ")
#     newstring = uppercase(string)
#     print(newstring)
# if __name__ == "__main__":
#     main()

def substring_search(string, substring):
    pos_list = []
    position = string.find(substring, 0)
    while True:
        if position == -1:
            break
        pos_list.append(position)
        position = string.find(substring, position + 1)
    return(pos_list)

def main():
    string = input("Enter a string: ")
    substring = input("Enter a substring: ")
    positions = substring_search(string, substring)
    print(positions)

if __name__ == "__main__":
    main()