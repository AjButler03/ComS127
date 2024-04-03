# Andrew Butler             11-17-2022
# Lab week 13 - exercise #1

# takes in an integer, converts it to binary, and returns the binary number in the form of a string.
def decToBin(num):
    binary_str = ""
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num //= 2
    return binary_str

def main():
    decimal_int = int(input("Enter an integer: "))
    binary_str = decToBin(decimal_int)
    print("{0} in binary is ".format(decimal_int) + binary_str)

if __name__ == "__main__":
    main()