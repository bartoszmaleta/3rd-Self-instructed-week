print('foo' * - 8)
print()

print('\n--------------------------------------------')
test = 'That\'s food for thought'
print(test)
print()

print('\n--------------------------------------------')
a = "Learning Python is super fun!"
print('super2' in a)

a = "Learning Python is super fun!"
print('super' in a)
print()

print('\n--------------------------------------------')
s = 'foo'
print(s in 'That\'s food for thought.')
print(s in 'That\'s good for now.')

print('\n--------------------------------------------')
a_ascii = ord('a')
print(a_ascii)

hash_ascii = ord('#')
print(hash_ascii)

euro = ord('€')
print(euro)

suming = ord('∑')
print(suming)

a_ascii_revert = chr(97)
print(a_ascii_revert)

hash_ascii_revert = chr(35)
print(hash_ascii_revert)

print('\n--------------------------------------------')
string1 = str(3+4j)
print(string1)

print('\n--------------------------------------------')
s = 'foobar'

print(s[0])
print(s[1])
print(len(s))
print(s[len(s)-1])
# print(s[7])     # string index out of range

print('\n-------------------------------------------- Minuses')
print(s[-1])
print(s[-2])
print(len(s))
print(s[-len(s)])
# print(s[-7])     # string index out of range

print('\n-------------------------------------------- Slicing')
word = 'foobar'
word_sliced = word[2:5]
print(word)
print(word_sliced)

print('\n-------------------------------------------- Slicing with parameters')
m = 1
n = 6
g = 2
print(word[m:n])
print(word[:g])
print(word[3:len(word)])

print('\n-------------------------------------------- Slicing and equals')
print(word[:4] + word[4:])
if (word[:4] + word[4:]) == word:
    print('This is the same')
print((word[:4] + word[4:]) == word)

print('\n-------------------------------------------- String id ')
word = 'foobar'
word2 = word[:]
print(id(word))
print(id(word2))
print(word is word2)

print('\n-------------------------------------------- Empty strings ')
print(word[2:2])    # Output: empty string
print(word[3:2])    # Output: empty string
# If the first index in a slice is greater than or equal to the second index, Python returns an empty string. 

print('\n-------------------------------------------- Negative indices')
print(word[-5:-2])
print(word[1:4])
print((word[-5:-2]) == word[1:4])

print('\n-------------------------------------------- Specifying a Stride in a String Slice')
print(word[0:6:2])
print(word[1:6:2])

print('\n-------------------------------------------- String indexes, stepper')

numbers_string = '12345' * 5
print(numbers_string)
print(numbers_string[::5])
print(numbers_string[4::5])

# Negative value as a step:
print(word[::-2])
print(word[5:0:-2])

print(numbers_string[::-5])
# reversing a string:
sentence = 'Interpolating Variables Into a String'
print(sentence)
sentence_revert = sentence[::-1]
print(sentence_revert)

print('\n-------------------------------------------- Interpolating Variables Into a String')
n = 20
m = 25
prod = n * m
print('The product of', n, 'and', m, 'is', prod)
print(f'The product of {n} and {m} is {prod}')
