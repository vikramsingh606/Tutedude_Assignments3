"""
Task 1: Calculate Factorial Using a Function
1.   Defines a function named factorial that takes a number as an argument and calculates 
     its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""


def funcFactorial(num):
    if num == 1:
        return 1
    else:
        while True:
            result = num * (funcFactorial(num - 1))
            return result


fNumber = funcFactorial(5)
print(f"Factorial of is {fNumber}\n")

"""
Task 2: Using the Math Module for Calculations
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
        o   Square root of the number
        o   Natural logarithm (log base e) of the number
        o   Sine of the number (in radians)
"""

import math as m


def funcModuleCalculations(userNumber):
    SquareRoot = m.sqrt(userNumber)
    Logarithm = m.log(userNumber)
    Sine = m.sin(userNumber)
    fData = (SquareRoot, Logarithm, Sine)
    return fData


try:
    userValue = int(input("Enter a number: "))
    numberTuple = funcModuleCalculations(userValue)
    print(f" SquareRoot is {int(numberTuple[0]) }")
    print(f" Natural Logarithm is {numberTuple[1] }")
    print(f" Sine is {numberTuple[2] }")
except ValueError:
    print("Kindly retry by entering a number")


