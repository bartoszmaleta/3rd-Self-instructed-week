print('\n-------------------------------------------- 1')
list_of_numbers = [1, 1, 2, 3, 3]
tuple_of_list_of_numbers = tuple(list_of_numbers)
print("a: ", tuple_of_list_of_numbers)
print(type(tuple_of_list_of_numbers))

a = tuple_of_list_of_numbers

print('\n-------------------------------------------- 2')
b = list(a)
print("b: ", b)
print(type(b))
print(len(b))

print('\n-------------------------------------------- 3')
c = set(b)
print("c: ", c)
print(type(c))
print(len(c))

print('\n-------------------------------------------- 4')
d = list(c)
print("d: ", d)
print(type(d))
print(len(d))

print('\n-------------------------------------------- 5')
range_1_10 = list(range(1, 11))
print(range_1_10)
print(type(range_1_10))
e = list(range_1_10)
print("e: ", e)
print(type(e))

print('\n-------------------------------------------- 6')
directory = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}
print(directory)
t = list(directory.items())
print(t)

print('\n-------------------------------------------- 7')
v = list(directory.values())
print(v)

print('\n-------------------------------------------- 8')
k = list(directory.keys())  # do not use it like this!!!
k = list(directory)

print(k)

print('\n-------------------------------------------- 9')
s = "antidisestablishmentarianism"
s_sorted = sorted(s)
print(s_sorted)
s_sorted_joined = ("".join(s_sorted))
print(s_sorted_joined)
s2 = s_sorted_joined
print(s2)

print('\n-------------------------------------------- 10')
print("the quick brown fox jumped over the lazy dog")
print("the quick brown fox jumped over the lazy dog".split())
