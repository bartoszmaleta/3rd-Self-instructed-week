import math

result = 8.5 + 7 // 3 - 2.5     # // ----> means we divide and cut everything after coma
print(result)   # its 8

print('------------------------------')
# ceil returns the closest integer greater than or equal to the number
# (so it always rounds up)
number_ceil = math.ceil(5.834)
number_ceil2 = math.ceil(5.254)
print(number_ceil)
print(number_ceil2)

print('------------------------------')
# floor returns the closest integer less than or equal to the number
# (so it always rounds down)
number_floor = math.floor(5.834)
number_floor2 = math.floor(5.245)
print(number_floor)
print(number_floor2)

print('------------------------------')
# round returns the closest integer to the number
# (so it rounds up or down)
# Note that this is a built-in function -- we don't need to import math to use
number_rounded = round(5.834)
number_rounded2 = round(5.245)
print(number_rounded)
print(number_rounded2)

print('------------------------------')
# This is OK
print(5)
print(4.5)

# This is not OK!!!!!!
# print("3" + 4)

# This is OK
print("3%d" % 4)    # concatenate "3" and "4" to get "34"

# or

print(int("3") + 4)     # add 3 and 4 to get 7

print('------------------------------')
# these 2 line will do the same
print('3%d' % 4)
print("3" + str(4)) 

print('------------------------------')
# This is OK
int("3")

# This is OK
int(3.7)

# This is not OK!!!!!
# int("3.7") # This is a string representation of a float, not an integer!

# We have to convert the string to a float first
int(float("3.7"))

my_flag = True

if my_flag:
    print("Hello!")

print('------------------------------')
my_number = 3

if my_number:
    print("My number is non-zero or empty string")
# bool is a function which converts values to booleans
# bool(34) # True
# bool(0) # False
# bool(1) # True

# bool("") # False
# bool("Jane") # True
# bool("0") # True!
# bool("False") # Also True