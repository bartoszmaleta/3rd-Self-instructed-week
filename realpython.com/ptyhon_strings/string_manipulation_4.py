# bytes OBJECTS

#  Each element in a bytes object is a small integer in the range 0 to 255.

b = b'foo barr baz'
print(b)
print(type(b))


# As with strings, you can use any of the single, double, or triple quoting mechanisms:

# >>> b'Contains embedded "double" quotes'
# b'Contains embedded "double" quotes'

# >>> b"Contains embedded 'single' quotes"
# b"Contains embedded 'single' quotes"

# >>> b'''Contains embedded "double" and 'single' quotes'''
# b'Contains embedded "double" and \'single\' quotes'

# >>> b"""Contains embedded "double" and 'single' quotes"""
# b'Contains embedded "double" and \'single\' quotes'

b = b'foo\xddbar'
print(b)

print(b[3])

print(int(0xdd))

print('\n-------------------------------------------- Bytes object')

b = rb'foo\xddbar'
print(b)

print(b[3])

print(chr(92))

print('\n-------------------------------------------- bytes(<s>, <encoding>)')
b = bytes('foo.bar', 'utf8')
print(b)
print(type(b))

b = bytes(8)
print(b)
print(type(b))
c = bytes(3)
print(c)

print('\n-------------------------------------------- bytes(<iterable>)')
b = bytes([100, 102, 104, 106, 108])
print(b)
print(b[2])

print('\n-------------------------------------------- Operations on bytes Objects')
b = b'abcde'

print(b'cd' in b)
print(b'foo' not in b)

b = b'abcde'
print(b + b'fghi')
print(b * 3)

print('\n-------------------------------------------- Operations on bytes Objects')
b = b'abcde'
print(b[2])
print(b[1:3])
print(len(b))
print(min(b))
print(max(b))

print('\n-------------------------------------------- Operations on bytes Objects')
# Many of the methods defined for string objects are valid for bytes objects as well:

# >>> b = b'foo,bar,foo,baz,foo,qux'

# >>> b.count(b'foo')
# 3

# >>> b.endswith(b'qux')
# True

# >>> b.find(b'baz')
# 12

# >>> b.split(sep=b',')
# [b'foo', b'bar', b'foo', b'baz', b'foo', b'qux']

# >>> b.center(30, b'-')
# b'---foo,bar,foo,baz,foo,qux----'


# Although a bytes object definition and representation is based on ASCII text, 
# it actually behaves like an immutable sequence of small integers in the range 0 to 255, inclusive.
#  That is why a single element from a bytes object is displayed as an integer:

# >>> b = b'foo\xddbar'
# >>> b[3]
# 221
# >>> hex(b[3])
# '0xdd'
# >>> min(b)
# 97
# >>> max(b)
# 221

print('\n-------------------------------------------- Operations on bytes Objects')
print(b[2:3])

print(list(b))

print('\n-------------------------------------------- Operations on bytes Objects - bytes.fromhex(<s>)')
b = bytes.fromhex(' aa 68 4682cc')
print(b)

print(list(b))
# Note: This method is a class method, not an object method. It is bound to the bytes class, not a bytes object. 
# You will delve much more into the distinction between classes,
#  objects, and their respective methods in the upcoming tutorials on object-oriented programming.
#   For now, just observe that this method is invoked on the bytes class, not on object b.

print('\n-------------------------------------------- Operations on bytes Objects - bytes.hex()')
b = bytes.fromhex(' aa 68 4682cc')
print(b)

print(b.hex())
print(type(b.hex()))

print('\n-------------------------------------------- bytearray Objects')
ba = bytearray('foo.bar.baz', 'UTF-8')
print(ba)

print(bytearray(6))
print(bytearray([100, 102, 104, 106, 108]))

ba[5] = 0xee
print(ba)

ba[8:11] = b'qux'
print(ba)

ba = bytearray(b'foo')
print(ba)
