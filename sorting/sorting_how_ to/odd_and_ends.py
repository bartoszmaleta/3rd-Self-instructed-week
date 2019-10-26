from operator import itemgetter, attrgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print('\n-------------------------------------------- ')
# The reverse parameter still maintains sort stability 
# (so that records with equal keys retain the original order). 
# Interestingly, that effect can be simulated without the 
# parameter by using the builtin reversed() function twice:

print()

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(data)

standard_way = sorted(data, key=itemgetter(0), reverse=True)
double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
assert standard_way == double_reversed
print(standard_way)

print()

print('\n-------------------------------------------- ')
# The sort routines are guaranteed to use __lt__() when making comparisons 
# between two objects. So, it is easy to add a standard sort 
# order to a class by defining an __lt__() method:

Student.__lt__ = lambda self, other: self.age < other.age
print(sorted(student_objects))

print('\n-------------------------------------------- ')
# Key functions need not depend directly on the objects being sorted. 
# A key function can also access external resources. For instance, 
# if the student grades are stored in a dictionary, they can be used 
# to sort a separate list of student names:

students = ["dave", "john", "jane"]
newgrades = {'john': 'F', 'jane': 'A', 'dave': 'C'}
sorted_students = sorted(students, key=newgrades.__getitem__)
print(sorted_students)