print()
s = 'foobar'
# s[3] = 'x'        # TypeError: 'str' object does not support item assignment

s = s[:3] + 'x' + s[4:]
print(s)

s_replace = s.replace('b', 'x')
print(s_replace)

print('\n-------------------------------------------- Built-in String Methods')

s = 'foO BaR BAZ quX'
s_cap = s.capitalize()
print(s_cap)

s = 'foo123#BAR#.'
s_cap = s.capitalize()
print(s_cap)

s_lower = s.lower()
print(s_lower)

s_swapcase = s.swapcase()
print(s_swapcase)

sentence = 'the sun also rises'
sentence_titled = sentence.title()
print(sentence_titled)

sentence2 = 'what\'s happened to ted\'s IBM stock?'
sentence_titled2 = sentence2.title()
print(sentence_titled2)

print(s.upper())

print('\n-------------------------------------------- Find and Replace')
word3 = 'foo goo moo'
print(word3)
print(word3.count('oo'))

print(word3.count('oo', 0, 8))

word4 = 'foobar'
word5 = word4.endswith('bar')
print(word5)
print(word4.endswith('baz'))
print(word4.endswith('oob', 0, 4))

print('\n-------------------------------------------- Find and Replace')
word = 'foo bar foo baz foo qux'
index_finder = word.find('foo')
index_finder2 = word.find('foo', 4)
# substring. s.find(<sub>) returns the lowest index in s where substring <sub> is found:
print(index_finder)
print(index_finder2)

# This method returns -1 if the specified substring is not found:
index_finder3 = word.find('grault')
print(index_finder3)
index_finder4 = word.find('foo', 4, 7)
print(index_finder4)

# find() similiar to index()
word2 = 'bar foo'
index_finder_by_index = word2.index('foo')
print(index_finder_by_index)

print('\n-------------------------------------------- Find and Replace')
# s.rfind(<sub>) returns the highest index in s where substring <sub> is found:
highest_index_of_word = word.rfind('foo')
print(highest_index_of_word)

highest_index_of_word_2 = word.rfind('fault')
print(highest_index_of_word_2)

highest_index_of_word_by_index = word.rfind('foo', 0, 14)
print(highest_index_of_word_by_index)

highest_index_of_word_by_index2 = word.rfind('foo', 10, 14)
print(highest_index_of_word_by_index2)

print('\n-------------------------------------------- Find')
# s.rindex(<sub>[, <start>[, <end>]])
# This method is identical to .rfind(), except that it raises an exception if <sub> is not found rather than returning -1:

# s.startswith(<prefix>[, <start>[, <end>]])

# Determines whether the target string starts with a given substring.

# When you use the Python .startswith() method, s.startswith(<suffix>) returns True if s starts with the specified <suffix> and False otherwise:

# >>> 'foobar'.startswith('foo')
# True
# >>> 'foobar'.startswith('bar')
# False

# The comparison is restricted to the substring indicated by <start> and <end>, if they are specified:

# >>> 'foobar'.startswith('bar', 3)
# True
# >>> 'foobar'.startswith('bar', 3, 2)
# False

sentence = 'abc123'
print(sentence.isalnum())

sentece2 = 'abc$123'
print(sentece2.isalnum())

sentence3 = ''      # empty, space ---> false
print(sentence3.isalnum())

print('\n-------------------------------------------- Find')
sentence4 = 'ABCabc'
print(sentence4.isalpha())
print(sentence.isalpha())

print('\n-------------------------------------------- Find')
word = '123'
print(word.isdigit())
print(sentence.isdigit())

print('\n-------------------------------------------- Find')

# s.isidentifier() returns True if s is a valid Python identifier according to the language definition, and False otherwise:

print('foo32'.isidentifier())   # True
print('32foo'.isidentifier())   # False
print('foo$32'.isidentifier())  # False

# Note: .isidentifier() will return True for a string that matches a Python keyword even though that would not actually be a valid identifier:

print('and'.isidentifier())
# True
# You can test whether a string matches a Python keyword using a function called iskeyword(), which is contained in a module called keyword. One possible way to do this is shown below:

# from keyword import iskeyword
# print(iskeyword('and'))     # True
# If you really want to ensure that a string would serve as a valid Python identifier, you should check that .isidentifier() is True and that iskeyword() is False.

# See Python Modules and Packages—An Introduction to read more about Python modules.

print('\n-------------------------------------------- Find')
word = 'abc'
word2 = 'abc1$d'
word3 = 'Abc'
print(word.islower())
print(word2.islower())
print(word3.islower())

# Determines whether the target string’s alphabetic characters are lowercase.

# s.islower() returns True if s is nonempty and all the alphabetic characters it contains are lowercase, and False otherwise. Non-alphabetic characters are ignored:

# >>> 'abc'.islower()
# True
# >>> 'abc1$d'.islower()
# True
# >>> 'Abc1$D'.islower()
# False

print('\n-------------------------------------------- Find')
# s.isprintable() returns True if s is empty or all the alphabetic characters it contains are printable.
# It returns False if s contains at least one non-printable character. Non-alphabetic characters are ignored:
print('a\tb'.isprintable())
# False
print('a b'.isprintable())
# True
print('a 2b'.isprintable())
# True
print(''.isprintable())
# True
print('a\nb'.isprintable())
# False

# Note: This is the only .isxxxx() method that returns True if s is an empty string. All the others return False for an empty string!!!!!!!!!!!!!!!!!

