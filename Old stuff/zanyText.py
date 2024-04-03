# Andrew Butler             9/2/2022
# Assignment #1

print("Zany Text!")
print()

# TODO: Have student print their name/ section when the script runs
print("By: Andrew Butler")
print("[COM S 127 B]")
print()

# Example 'Zany Text' - gathering input
print("Once upon a time, there was a <noun>.")
noun1 = input("noun: ")
print("It was a <adjective>, <adjective>, <adjective>", noun1)
adjective1 = input("adjective: ")
adjective2 = input("adjective: ")
adjective3 = input("adjective: ")
print("And, one day, it <past tense action> all over the <noun>!")
verb1 = input("past tense action: ")
noun2 = input("noun: ")
print()

# Example 'Zany Text' - printing the final string
print("Once upon a time, there was a", 
        noun1, 
        ". It was a", 
        adjective1, ",", 
        adjective2, ",", 
        adjective3, 
        noun1, 
        ". And, one day it", 
        verb1, 
        "all over the", 
        noun2,"!")
print()

# TODO: Make three more 'Zany Texts' like the one above, and have all four run/ print out in order. 
# There should be at least four (4) 'Zany Texts' in a completed assignment.

# Custom Zanytext No. 1
print("The <team name> are down 4-3 in the bottom of the ninth.")
team = input("Enter a team name: ")
print("2 out. <player> is up to bat. The count is <balls>-<strikes>.")
player = input("Enter player name: ")
balls = input("Enter a number between 0 and 3: ")
strikes = input("Enter a number between 0 and 2: ")
print()

print("The", 
        team, 
        "are down 4-3 in the bottom of the ninth. 2-out.", 
        player,
        "is up to bat. The count is",
        balls,
        "-",
        strikes,
        ". Here's the pitch- it's hit hard- straight into the center fielders glove.")
print()

# Custom Zanytext No. 2
print("<firstname><lastname>'s favorite movie is <favmovie>, and their favorite food is <favfood>.")
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
favmovie = input("Enter your favorite movie: ")
favfood = input("Enter your favorite food: ")
print()

print(f"{firstname} {lastname}'s favorite movie is {favmovie}, and their favorite food is {favfood}.")
print()

# Custom Zanytext No. 3
print("We're going to do some basic math. Here is some addition: <1st number> + <2nd number> = <sum>.")
num1 = int( input("Enter an integer for the first number: "))
num2 = int( input("Enter an integer for the second number: "))
sum = num1 + num2
print("Here is some multiplication: <3rd number> * <4th number> = <product>.")
num3 = int( input("Enter an integer for the 3rd number: "))
num4 = int( input("Enter an integer for the 4th number: "))
print()

print("we're going to do some basic math. Here is some addition: {0} + {1} = {2},".format(num1, num2, (num1 + num2)),
"and here is some multiplication: {0} * {1} = {2}.".format(num3, num4, (num3*num4)))