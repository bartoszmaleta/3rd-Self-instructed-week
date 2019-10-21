letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

thing = 0
while thing < len(letters):
    print(letters[thing])
    thing += 1

print('-------------------------')

for element in letters:
    print(element)

print('-----------------------------')

for letter in letters:
    print(letter)
    if letter == 'e':
        print('this is e!')

print('-----------------------------')

for letter in letters:
    print(letter, end='')
    if letter == 'e':
        print('this is e!')

print('-----------------------------')

for i in range(13):
    print(i)

print('-----------------------------')

for i in range(33, 35):
    print(i)

print('-----------------------------')

for i in range(21, 31, 2):
    print(i)