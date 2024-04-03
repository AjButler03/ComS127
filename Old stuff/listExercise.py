# Andrew Butler             10-14-2022
# List of numbers exercise

def fnListN(n, nNumbers):
    for i in range(n):
        num = int(input("Enter an integer: "))
        nNumbers.append(num)
    return(nNumbers)

def fnSquare(nSquaredNumber, nNumbers):
    for i in range(len(nNumbers)):
        nSquaredNumber.append(nNumbers[i]**2)
    return(nSquaredNumber)

def main():
    nNumbers = []
    nSquaredNumber = []
    n = int( input("How many numbers will be entered: "))
    fnListN(n, nNumbers)
    fnSquare(nSquaredNumber, nNumbers)
    print(nNumbers)
    print(nSquaredNumber)

if __name__ == "__main__":
    main()