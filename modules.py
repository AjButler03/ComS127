# Andrew Butler             11-2-2022
# modules demo

import my_math

def main():
    x = float(input("Enter a float: "))
    y = int(input("Enter an integer: "))
    z = int(input("Enter an integer: "))
    value = my_math.val(x, y, z)
    print(value)

if __name__ == "__main__":
    main()