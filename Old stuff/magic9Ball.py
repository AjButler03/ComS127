# Andrew Butler             9-12-2022
# Assignment #2

print("Welcome to the Magic 9 Ball...")
print()

# TODO: Have student print their name/ section when the script runs
print("By: Andrew Butler")
print("[COM S 127 B]")
print()

print("What would you like to do?")
print()
choice = input("[c]alculator, [p]rediction, [q]uit: ")
print()

# initial choice tasks ------------------------------------------------------------------------------------------------------------------------
# TODO: use conditional logic to determine which function of the Magic 9 Ball to use: [c]alculator, [p]rediction, [q]uit
# - create a section of code that executes if the user enters 'c' as their initial choice
# - create a section of code that executes if the user enters 'p' as their initial choice
# - create a section of code that executes if the user enters 'q' as their initial choice
# TODO: add another section of code where if the user does not enter "c", "p", or "q" in their initial choice, the script will print out an error message stating: 
# "ERROR: I did not understand your input... Please try again..." or something similar (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'c' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'c' section, take in input from the user for one of six calculations: [+], [-], [*], [/], [%], [**]
# TODO: if the user does not enter "+", "-", "*", "/", "%", or "**" in their calculation choice, print out an error message stating: 
# "ERROR: You must enter either \"+\", \"-\", \"*\", \"/\", \"%\", or \"**\"" or something similar (use your imagination)
# TODO: depending on the input from the step above, use conditional logic to determine which calculation to perform
# TODO: program code sections for each calculation type which takes in input for the left hand side and right hand side
# of the operator, perform the calculation, then print the result
# TODO: for / and % use conditional logic to check if the right hand side of the expression is zero (0) and print an error if it is
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'p' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'p' section, take in input from the user asking them "What is your question?: " or something similar (use your imagination)
# TODO: print a string stating print("As far as '", question, "' is concerned, I predict: ") or something similar (use your imagination)
# TODO: use then length of the question string the user input to generate a 'prediction selection value' within the following range: 
# from 0 through (<the number of predictions>-1)
# HINT: there is a built in function to find the range of a string
# HINT: one of the operators used in the 'c' section of the script will return a value within the range 'from 0 through (<the number of predictions>-1)'
# when applied to <the length of the question string> on the left side of the operator, and <the number of predictions> on the right side
# TODO: write at least ten (10) 'predictions' and use conditional logic to select which one to print after the 'prediction selection value'
# from above is calculated (use your imagination)
# TODO: if the computation to produce a 'prediction selection value' creates a value outside the range 'from 0 through (<the number of predictions>-1)'
# then have the script print an error message to that effect. NOTE: If the calculation of a 'prediction selection value' is done properly, this 
# error message should **never** be seen.
# HINT: if you write ten (10) 'predictions,' then <the number of predictions> will be 10. This means that the range of the 'prediction 
# selection value' will be between 0 and 9. After selecting a value between 0 and 9 by way of the length of the 'question' string, one of
# the operators from the 'c' option, and <the number of predictions>, you will print out a 'prediction' corresponding to this value.
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'q' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'q' option, print out a message stating "Maybe next time...", or "Goodbye!", or something else to that effect 
# (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------

if choice == "c":

    # Getting an operator for calculation from user
    calc_type = input("Enter the type of calculation: [+], [-], [*], [/], [%], [**]: ")

    # performing calculations and printing result
    if calc_type == "+":
        num1 = float( input("Enter a number: "))
        num2 = float( input("Enter a number: "))
        result = num1 + num2
        print("{0} + {1} = {2}.".format(num1, num2, result))
    elif calc_type == "-":
        num1 = float( input("Enter a number: "))
        num2 = float( input("Enter a number: "))
        result = num1 - num2
        print("{0} - {1} = {2}.".format(num1, num2, result))
    elif calc_type == "*":
        num1 = float( input("Enter a number: "))
        num2 = float( input("Enter a number: "))
        result = num1 * num2
        print("{0} * {1} = {2}.".format(num1, num2, result))
    elif calc_type == "/":
        num1 = float( input("Enter a number: "))
        num2 = float( input("Enter a number: "))

        # checking to make sure that num2 is not zero for division, posting error if it is
        if num2 != 0.0:
            result = num1 / num2
            print("{0} / {1} = {2}.".format(num1, num2, result))
        else:
            print("Error: cannot divide by zero. Please try again.")
    elif calc_type == "%":
        num1 = float( input("Enter a number: "))
        num2 = float( input("Enter a number: "))

        # checking to make sure that num2 is not zero for division, posting error if it is
        if num2 != 0.0:
            result = num1 % num2
            print("{0} % {1} = {2}.".format(num1, num2, result))
        else:
            print("Error: cannot divide by zero. Please try again.")
    elif calc_type == "**":
        num1 = float( input("Enter a number: "))
        num2 = float( input("Enter a number: "))
        result = num1 ** num2
        print("{0} ** {1} = {2}.".format(num1, num2, result))
    else:
        print("Error: Invalid operator. Please try again and enter [+], [-], [*], [/], [%], or [**].")

elif choice == "p":

    # User inputs question
    p_question = str( input("What is your question?: "))

    # calculating prediction_selection variable to decide which prediction to output
    prediction_selection = len(p_question) % 10

    # Determining and printing response
    if prediction_selection == 0:
        predict = "Ask again later."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 1:
        predict = "As I see it, yes."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 2:
        predict = "Don't count on it."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 3:
        predict = "It is unclear."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 4:
        predict = "The outlook is good."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 5:
        predict = "You may rely on it."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 6:
        predict = "Your odds aren't great."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 7:
        predict = "Like a roll of 7 on a pair of dice, it is most likely."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 8:
        predict = "Sure thing, pal."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    elif prediction_selection == 9:
        predict = "Definitely not."
        print("Regarding your question, \"{0}\": {1}".format(p_question, predict))
    else:
        print("Error predicting. Please try again.")

elif choice == "q":
    print("Quitting? Until next time...")

else:
    print("Error: Unknown request. Please restart and input [c] for calculator, [p] for prediction, or [q] to quit.")