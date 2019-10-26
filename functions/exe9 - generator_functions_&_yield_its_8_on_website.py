print('\n-------------------------------------------- 1')


def my_gen(n):
    i = n

    while i >= 0:
        yield i
        i -= 1
    
    
for x in my_gen(3):
    print(x)