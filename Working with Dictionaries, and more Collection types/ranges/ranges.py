# print the integers from 0 to 9
print(list(range(10)))

# print the integers from 1 to 10
print(list(range(1, 11)))

# print the odd integers from 1 to 10
print(list(range(1, 11, 2)))

# We create a range by calling the range function. As you can see, if we pass a single parameter to the range function,
# it is used as the upper bound. If we use two parameters, the first is the lower bound and the second is the upper bound.
# If we use three, the third parameter is the step size. The default lower bound is zero,
# and the default step size is one. Note that the range includes the lower bound and excludes the upper bound.