# In Py2.x, sort allowed an optional function which can be 
# called for doing the comparisons. That function should take two 
# arguments to be compared and then return a negative value for 
# less-than, return zero if they are equal, or return a positive 
# value for greater-than. For example, we can do:

# def numeric_compare(x, y):
#     return x - y
# sorted([5, 2, 4, 1, 3], cmp=numeric_compare) # doctest: +SKIP

# >>> def reverse_numeric(x, y):
# ...     return y - x
# >>> sorted([5, 2, 4, 1, 3], cmp=reverse_numeric) # doctest: +SKIP
# [5, 4, 3, 2, 1]

# When porting code from Python 2.x to 3.x, the situation can arise when you have the user supplying a comparison function and you need to convert that to a key function. The following wrapper makes that easy to do:

# def cmp_to_key(mycmp):
#     'Convert a cmp= function into a key= function'
#     class K:
#         def __init__(self, obj, *args):
#             self.obj = obj
#         def __lt__(self, other):
#             return mycmp(self.obj, other.obj) < 0
#         def __gt__(self, other):
#             return mycmp(self.obj, other.obj) > 0
#         def __eq__(self, other):
#             return mycmp(self.obj, other.obj) == 0
#         def __le__(self, other):
#             return mycmp(self.obj, other.obj) <= 0
#         def __ge__(self, other):
#             return mycmp(self.obj, other.obj) >= 0
#         def __ne__(self, other):
#             return mycmp(self.obj, other.obj) != 0
#     return K
# To convert to a key function, just wrap the old comparison function:

# >>> sorted([5, 2, 4, 1, 3], key=cmp_to_key(reverse_numeric))
# [5, 4, 3, 2, 1]