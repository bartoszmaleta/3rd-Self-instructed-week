import math

print('\n-------------------------------------------- 1 mine')


def hypotenuse(a, b):
    try:
        a_square = a ** 2 
        b_square = b ** 2

        sum_of_two_numbers_squared = a_square + b_square
        # print(sum_of_two_numbers_squared)

        return math.sqrt(sum_of_two_numbers_squared) 
    except TypeError:
        return None

# a = 2.0
# b = 3


print(hypotenuse(2.2, 3.3))
print(hypotenuse("str1", "str2"))
print(hypotenuse("str3", 2))
# print(hypotenuse(2, 3))
# print(hypotenuse(2, 3.3))