import math

a = lambda: 3

# it is the same as:


def a():
    return 3


print('\n-------------------------------------------- ')
b = lambda x, y: x + y

# is the same as:


def b(x, y):
    return x + y


print('\n-------------------------------------------- 1.1.')
a = lambda x: x**2

print('\n-------------------------------------------- 1.2.')
b = lambda x, y: math.sqrt(x**2 + y**2)
# Z^2 =  X^2 + Y^2

print('\n-------------------------------------------- 1.3.')
c = lambda *args: sum(args)/len(args)

print('\n-------------------------------------------- 1.4')
d = lambda s: "".join(set(s))

print('\n-------------------------------------------- 2.1.')


def a(x):
    result = x**2
    return result


print('\n-------------------------------------------- 2.2.')


def b(x, y):
    result = math.sqrt(x**2 + y**2)
    return result


print('\n-------------------------------------------- 2.3.')


def c(*args):
    result = sum(args)/len(args)
    return result


print('\n-------------------------------------------- 2.4.')


def d(s):
    result = "".join(set(s))
    return result

