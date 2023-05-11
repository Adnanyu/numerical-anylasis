import math
while True:
    try:
        # Ask the user for the first number
        num1 = float(input("Enter the first number: "))

        # Ask the user for the second number
        num2 = float(input("Enter the second number: "))

        # Calculate the absolute error
        abs_error = abs(num1 - num2)

#         Calculate the relative error
        rel_error = abs_error / num1

        # Round the relative error to 7 significant digits
        rel_error_rounded = round(rel_error, -int(math.floor(math.log10(abs(rel_error))))+6)

#         Output the relative error as a 7-digit floating-point number and in scientific notation
        print("RE: {:.5e}".format(rel_error_rounded))
    except EOFError:
        print('')
