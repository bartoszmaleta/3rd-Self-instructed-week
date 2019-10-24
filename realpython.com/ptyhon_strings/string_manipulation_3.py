# .isspace()

print(' \t \n '.isspace())      # True
print('   a    '.isspace())     # False


# However, there are a few other ASCII characters that qualify as whitespace, and if you account for Unicode characters, there are quite a few beyond that:

# >>> '\f\u2005\r'.isspace()
# True
# ('\f' and '\r' are the escape sequences for the ASCII Form Feed and Carriage Return characters; '\u2005' is the escape sequence for the Unicode Four-Per-Em Space.)

print('\n-------------------------------------------- Find')
# s.istitle() returns True if s is nonempty, the first alphabetic character of each word is uppercase, and all other alphabetic characters in each word are lowercase. It returns False otherwise:

# >>> 'This Is A Title'.istitle()
# True
# >>> 'This is a title'.istitle()
# False
# >>> 'Give Me The #$#@ Ball!'.istitle()
# True

print('\n-------------------------------------------- Find')
# s.isupper()

print('\n-------------------------------------------- String formatting')

word = 'foobar'
print(word.center(10))
print(word.center(10, '-'))
print(word.center(3))   # If s is already at least as long as <width>, it is returned unchanged!!!!
# >>> 'foo'.center(2)
# 'foo'

print('a\tb\tc'.expandtabs())
print('a\tb\tc')
print('a\tb\tc'.expandtabs(15))
print('aaa\tbbb\tccc'.expandtabs(tabsize=5))
print('aaa\tbbb\tccc'.expandtabs(tabsize=4))
print('aaa\tbbb\tccc'.expandtabs(tabsize=3))
print('aaa\tbbb\tccc'.expandtabs(tabsize=2))
print('aaa\tbbb\tccc'.expandtabs(tabsize=1))

print('\n-------------------------------------------- String formatting')
print(word.ljust(10))
print(word.ljust(10, '-'))
# If s is already at least as long as <width>, it is returned unchanged:

sentence = '   foo bar baz----'
print(sentence)
sentence_lstrip = sentence.lstrip()
print(sentence_lstrip)
print('\t\nfoo\t\nbar\t\nbaz'.lstrip())
print('http://www.realpython.com'.lstrip('/:pth'))

print('\n-------------------------------------------- String formatting')
print('foo bar foo baz foo qux'.replace('foo', 'grault'))
print('foo bar foo baz foo qux'.replace('foo', 'grault', 2))

print('\n-------------------------------------------- String formatting')
# s.rjust(<width>[, <fill>])

# Right-justifies a string in a field.

# s.rjust(<width>) returns a string consisting of s right-justified in a field of width <width>. By default, padding consists of the ASCII space character:

# >>> 'foo'.rjust(10)
# '       foo'

print('\n-------------------------------------------- String formatting')
# s.rstrip() returns a copy of s with any whitespace characters removed from the right end:

# >>> '   foo bar baz   '.rstrip()
# '   foo bar baz'
# >>> 'foo\t\nbar\t\nbaz\t\n'.rstrip()
# 'foo\t\nbar\t\nbaz'
print('foo.$$$;'.rstrip(';$.'))
print('foo.$$$;'.rstrip('.$$$;'))
word = 'foobarbaz'
print(word.rstrip('baz'))

# s.strip() is essentially equivalent to invoking s.lstrip() and s.rstrip() in succession. Without the <chars> argument, it removes leading and trailing whitespace:
s = '   foo bar baz\t\t\t'
s2 = s.strip()
print(s2)

print('www.realpython.com'.strip('w.moc'))

# Note: When the return value of a string method is another string, as is often the case, methods can be invoked in succession by chaining the calls:

# >>> '   foo bar baz\t\t\t'.lstrip().rstrip()
# 'foo bar baz'
# >>> '   foo bar baz\t\t\t'.strip()
# 'foo bar baz'

# >>> 'www.realpython.com'.lstrip('w.moc').rstrip('w.moc')
# 'realpython'
# >>> 'www.realpython.com'.strip('w.moc')
# 'realpython'

print('\n-------------------------------------------- String formatting')
print('42'.zfill(5))
print('+42'.zfill(8))
# If s is already at least as long as <width>, it is returned unchanged:
# >>> '-42'.zfill(3)
# '-42'

print('\n-------------------------------------------- String formatting')
print(', '.join(['foo', 'bar', 'baz', 'qux']))

list_of_letters = []
list_of_letters.append('c')
list_of_letters.append('o')
list_of_letters.append('r')
list_of_letters.append('g')
list_of_letters.append('e')
print(list_of_letters)

print(':'.join('corge'))
# print('---'.join(['foo', 23, 'bar'])) # wont work!!!
print('---'.join(['foo', str(23), 'bar']))

print('\n-------------------------------------------- String formatting')
print('foo.bar'.partition('.'))
print('foo@@bar@@baz'.partition('@@'))
print('foo.bar'.partition('@@'))

print('\n-------------------------------------------- String formatting')
# s.rpartition(<sep>) functions exactly like s.partition(<sep>), except that s is split at the last occurrence of <sep> instead of the first occurrence:
print('foo@@bar@@baz'.partition('@@'))
print('foo@@bar@@baz'.rpartition('@@'))

print('\n-------------------------------------------- String formatting')
print('foo bar baz qux'.rsplit())
print('foo\n\tbar   baz\r\fqux'.rsplit())
print('foo.bar.baz.qux'.rsplit(sep='.'))
print('foo...bar'.rsplit(sep='.'))
print('foo\t\t\tbar'.rsplit())
print('www.realpython.com'.rsplit(sep='.', maxsplit=1))
print('www.realpython.com'.rsplit(sep='.', maxsplit=-1))
print('www.realpython.com'.rsplit(sep='.'))

print('\n-------------------------------------------- String formatting')
# s.split() behaves exactly like s.rsplit(), except that if <maxsplit> is specified, splits are counted from the left end of s rather than the right end:

print('www.realpython.com'.split('.', maxsplit=1))
print('www.realpython.com'.rsplit('.', maxsplit=1))

# s.splitlines([<keepends>])

# Breaks a string at line boundaries.

# s.splitlines() splits s up into lines and returns them in a list. Any of the following characters or character sequences is considered to constitute a line boundary:

print('foo\nbar\r\nbaz\fqux\u2028quux'.splitlines())
print('foo\f\f\fbar'.splitlines())
print('foo\nbar\nbaz\nqux'.splitlines(True))
print('foo\nbar\nbaz\nqux'.splitlines(1))