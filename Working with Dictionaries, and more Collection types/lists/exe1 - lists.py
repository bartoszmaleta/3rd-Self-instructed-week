print('\n-------------------------------------------- 1, 2')
a = [3, 5, 7]
b = [4, 6, 8]
print(a)
print(b)

ab = a + b
print(ab)

print('\n-------------------------------------------- 3')
c2 = ab.sort()
c = sorted(ab)

print('This is c: ', c)
print(c2)  # Dont work!! shouldnt!!!

print('\n-------------------------------------------- 4')
d = list(reversed(c))
print(d)

print('\n-------------------------------------------- 5')
print(c)
c.pop(3)
c.insert(3, 42)
print(c)

print('\n-------------------------------------------- 6')
print(d)
d.append(10)
print(d)

print('\n-------------------------------------------- 7')
print(c)
c.extend([7, 8, 9])
c.append([7, 8, 9])  # not good!
print(c)

print('\n-------------------------------------------- 8')
print(c[:3])

print('\n-------------------------------------------- 9')
print(d)
print(d[-1])

print('\n-------------------------------------------- 10')
print(len(d))