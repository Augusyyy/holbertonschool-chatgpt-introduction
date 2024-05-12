#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the number 'n'.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n multiplied by the factorial of n-1


# Takes an integer from command line argument, calculates its factorial, and prints it.
f = factorial(int(sys.argv[1]))
print(f)
