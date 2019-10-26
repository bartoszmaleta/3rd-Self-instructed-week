# THE STACK
# https://python-textbok.readthedocs.io/en/1.0/Functions.html#exercise-3
# RECURSION
# We can make a function call itself. This is known as recursion. A common 
# example is a function which calculates numbers in the Fibonacci sequence: 
# the zeroth number is 0, the first number is 1, and each subsequent number 
# is the sum of the previous two numbers:


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Writing fail-safe recursive functions is difficult. What if we called the 
# function above with a parameter of -1? We haven’t included any error checking 
# which guards against this, so we would skip over the end cases and try to 
# calculate fibonacci(-2), fibonacci(-3), and keep going.

# Any recursive function can be re-written in an iterative way which avoids 
# recursion. For example:


def fibonacci2(n):
    current, next = 0, 1

    for i in range(n):
        current, next = next, current + next

    return current


# This function uses iteration to count up to the desired value of n, 
# updating variables to keep track of the calculation. All the iteration 
# happens within a single instance of the function. Note that we assign 
# new values to both variables at the same time, so that we can use both 
# old values to calculate both new values on the right-hand side.