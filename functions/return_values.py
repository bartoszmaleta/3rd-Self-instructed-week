# We can rewrite the print_sum function to return the result of its 
# addition instead of printing it:


def add(a, b):
    return a + b


# We use the return keyword to define a return value. To access this value 
# when we call the function, we have to assign the result of the 
# function to a variable:

a = 2.0
b = 3

c = add(a, b)

# Here the return value of the function will be assigned to c when the 
# function is executed.

print(c)

print('\n-------------------------------------------- ')

# A function can only have a single return value, but that value can be 
# a list or tuple, so in practice you can return as many different values 
# from a function as you like. It usually only makes sense to return multiple 
# values if they are tied to each other in some way. If you place several 
# values after the return statement, separated by commas, they will 
# automatically be converted to a tuple. Conversely, you can assign a tuple 
# to multiple variables separated by commas at the same time, so you can 
# unpack a tuple returned by a function into multiple variables:


def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


# you can do this
q, r = divide(35, 4)
print(q)
print(r)

print('\n-------------------------------------------- ')
# but you can also do this
result = divide(67, 9)
q1 = result[0]
q2 = result[1]
print(result)
print(q1)
print(q2)

print('\n-------------------------------------------- ')
# by the way, you can also do this
a, b = (1, 2)
# or this
c, d = [5, 6]

print('\n-------------------------------------------- ')


def print_a_message(message):
    print(message)


mystery_output = print_a_message("Boo!")
print(mystery_output)

print('\n-------------------------------------------- ')
# When a return statement is reached, the flow of control immediately 
# exits the function – any further statements in the function body will be 
# skipped. We can sometimes use this to our advantage to reduce the
# number of conditional statements we need to use inside a function:


def divide(dividend, divisor):
    if not divisor:
        return None, None  # instead of dividing by zero

    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


print(divide(30, 14))

print('\n-------------------------------------------- ')
# This technique can be useful whenever we want to check parameters at the 
# beginning of a function – it means that we don’t have to indent the main 
# part of the function inside an else block. Sometimes it’s more appropriate 
# to raise an exception instead of returning a value like None if there is 
# something wrong with one of the parameters:


def divide(dividend, divisor):
    if not divisor:
        raise ValueError("The divisor cannot be zero!")

    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


print(divide(30, 14))
