from operator import itemgetter, attrgetter

print()
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


print('\n-------------------------------------------- ')
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(student_tuples)

print('\n-------------------------------------------- 1 tuple')

student_tuples_sorted_by_index_of_age = sorted(student_tuples, key=itemgetter(2))
print(student_tuples_sorted_by_index_of_age)

print('\n-------------------------------------------- 1 object')
student_objects_sorted_by_age = sorted(student_objects, key=attrgetter("age"))
print(student_objects_sorted_by_age)
print()

print('\n-------------------------------------------- 2 tuple')
student_tuples_sorted_by_grade_then_by_age_index = sorted(student_tuples, key=itemgetter(1, 2))
print(student_tuples_sorted_by_grade_then_by_age_index)

print('\n-------------------------------------------- 2 object')
student_objects_sorted_by_grade_then_by_age_name = sorted(student_objects, key=attrgetter("grade", "age"))
print(student_objects_sorted_by_grade_then_by_age_name)

print('\n-------------------------------------------- tuple - Ascending and Descending')

reverse_students_tuples = sorted(student_tuples, key=itemgetter(2), reverse=True)
print(reverse_students_tuples)

print('\n-------------------------------------------- objects - Ascending and Descending')
reverse_students_objects = sorted(student_objects, key=attrgetter("age"), reverse=True)
print(reverse_students_objects)

print('\n-------------------------------------------- Sort Stability and Complex Sorts')
data = [("red", 1), ("blue", 1), ("red", 2), ("blue", 2)]
print(data)

sorted_data = sorted(data, key=itemgetter(0))
print(sorted_data)

print('\n-------------------------------------------- Sort Stability and Complex Sorts')
print(student_objects)

sorted_by_age_student_objects = sorted(student_objects, key=attrgetter("age"))
print(sorted_by_age_student_objects)  # sort on secondary key

sorted_by_age_student_objects_by_grade = sorted(sorted_by_age_student_objects, key=attrgetter("grade"), reverse=True)
print(sorted_by_age_student_objects_by_grade)  # now sort on primary key, descending

print('\n-------------------------------------------- Sort Stability and Complex Sorts')


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs


multisorted_student_objects = multisort(list(student_objects), (("grade", True), ("age", False)))
print(multisorted_student_objects)

print('\n-------------------------------------------- The Old Way Using Decorate-Sort-Undecorate')
decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
print(decorated)  # decorate

sorted_decorated = decorated.sort()
print(sorted_decorated)  # sort

loop_sorted_decorated = [student for grade, i, student in decorated]
print(loop_sorted_decorated)  # undecorate 

print("The Old Way Using the cmp Parameter".lower())
