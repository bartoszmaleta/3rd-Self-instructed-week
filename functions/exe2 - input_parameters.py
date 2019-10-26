import math

print('\n-------------------------------------------- 1 mine')


def hypotenuse(a, b):
    a_square = a ** 2 
    b_square = b ** 2

    sum_of_two_numbers_squared = a_square + b_square
    print(sum_of_two_numbers_squared)

    sqrt_of_sum_of_two_numbers_squared = math.sqrt(sum_of_two_numbers_squared) 
    print(sqrt_of_sum_of_two_numbers_squared)


# a = 2.0
# b = 3

hypotenuse(2.2, 3.3)
hypotenuse(2, 3)
hypotenuse(2, 3.3)

print('\n-------------------------------------------- 1 answer')


def hypotenuse(x, y):
    print(math.sqrt(x**2 + y**2))


hypotenuse(12.3, 45.6)
hypotenuse(2, 3)
hypotenuse(12, 34.5)