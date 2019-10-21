a = 0


def my_function():
    a = 3
    print(a)


my_function()  # 3

print(a)  # 0


b = 4

print('------------------------------------')


def my_function2():
    global b
    b = 5
    print(b)


my_function2()

print(b)

print('------------------------------------')


# CANT DO THIS LIKE THIS
# c = 6


# def my_function3():
#     print(c)
#     c = 7
#     print(c)


# my_function3()
