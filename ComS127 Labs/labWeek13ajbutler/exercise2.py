# Andrew Butler             11-17-2022
# Lab week 13 - exercise #2

# takes in a binary number in the form of a string, converts it to a decimal number, and outputs that as an integer.
def binToDec(binary_str):
    num = 0
    for character in binary_str:
        num = num * 2 + int(character)
    return num


def main():
    binary_str = input("Enter a binary number: ")
    decimal_num = binToDec(binary_str)
    print(binary_str + " is {0} in decimal".format(decimal_num))

if __name__ == "__main__":
    main()