# Consider this simple function which returns a range of numbers as a list:


def my_list(n):
    i = 0
    l = []

    while i < n:
        l.append(i)
        i += 1

    return l


print('\n-------------------------------------------- ')
# This function builds the full list of numbers and returns it. We can change 
# this function into a generator function while preserving a very similar syntax, like this:


def my_gen(n):
    i = 0

    while i < n:
        yield i
        i += 1


print('\n-------------------------------------------- ')
# The first important thing to know about the yield statement is that if we use it in a function, 
# that function will return a generator. We can test this by using the type function on the 
# return value of my_gen. We can also try using it in a for loop, like we would use any other 
# generator, to see what sequence the generator represents:

g = my_gen(3)

print(type(g))

for x in g:
    print(x)