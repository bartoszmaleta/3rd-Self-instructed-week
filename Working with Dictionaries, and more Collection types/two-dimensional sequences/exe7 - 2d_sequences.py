print('\n-------------------------------------------- 1')
first_tuple = ('Monday')
second_tuple = ('Tuesday', 'Wednesday')
third_tuple = ('Thursday', 'Friday', 'Saturday')
print(first_tuple)
print(second_tuple)
print(third_tuple)

a = [first_tuple, second_tuple, third_tuple]
print('list of tuples: ', a)
print('\n-------------------------------------------- 2')
b = a[1][1]
print('second element of second element of a: ', b)

print('\n-------------------------------------------- ')
b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(b)
print(b[0][-2:])
