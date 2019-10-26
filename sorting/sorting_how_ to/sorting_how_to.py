list_of_numbers = [5, 2, 3, 1, 4]
print(list_of_numbers)

sorted_list_of_numbers = sorted(list_of_numbers)

print(sorted_list_of_numbers)

print('\n-------------------------------------------- ')
# You can also use the list.sort() method. It modifies the list 
# in-place (and returns None to avoid confusion). Usually it’s less 
# convenient than sorted() - but if you don’t need the original list, 
# it’s slightly more efficient.

sorted2_list_of_numbers = list_of_numbers.sort()
print(sorted2_list_of_numbers)

# Another difference is that the list.sort() method is only defined for 
# lists. In contrast, the sorted() function accepts any iterable.

sorted_dict = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
print(sorted_dict)

print('\n-------------------------------------------- ')
some_string = "This is a test string from Bartosz"
print(some_string)
print(sorted(some_string.split(), key=str.lower))

print('\n-------------------------------------------- ')
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(student_tuples)

# sort by age
sorted_student_tuples = sorted(student_tuples, key=lambda student: student[2])
print(sorted_student_tuples)

print('\n-------------------------------------------- ')


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


print('\n-------------------------------------------- ')
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(student_objects)
sorted_student_objects = sorted(student_objects, key=lambda student: student.age)   # sort by age
print(sorted_student_objects)

print('\n-------------------------------------------- ')
