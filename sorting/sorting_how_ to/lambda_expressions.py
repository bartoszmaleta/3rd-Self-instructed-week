# Small anonymous functions can be created with the lambda keyword. 
# This function returns the sum of its two arguments: lambda a, b: a+b. 
# Lambda functions can be used wherever function objects are required. 
# They are syntactically restricted to a single expression. 
# Semantically, they are just syntactic sugar for a normal function definition. 
# Like nested function definitions, lambda functions can reference 
# variables from the containing scope:

print()


def make_incrementator(n):
    return lambda x: x + n


f = make_incrementator(42)

print(f(0))

print(f(1))

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- ')
# The above example uses a lambda expression to return a function. 
# Another use is to pass a small function as an argument:

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)

sorted_pairs = pairs.sort(key=lambda pair: pair[1])
print(sorted_pairs)
