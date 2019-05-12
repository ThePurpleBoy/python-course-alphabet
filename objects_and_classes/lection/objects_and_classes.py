<<<<<<< HEAD
from utils import describe_object
=======

>>>>>>> f07bec3747a40695b27082ca48aae333e38da811


# This is object of class
# There is only one object of the same class.
<<<<<<< HEAD
class Student:
    pass

=======
from utils import describe_object


class Student:
    def __init__(self, name):
        pass
>>>>>>> f07bec3747a40695b27082ca48aae333e38da811

print(describe_object(name="Student", obj=Student))
# This is instances of class Student

# It could be a lot of instances of one class
student_1 = Student()
<<<<<<< HEAD
student_2 = Student()
=======

student_2 = Student()

>>>>>>> f07bec3747a40695b27082ca48aae333e38da811
student_3 = Student()

print(describe_object("student_1", student_1))
print(describe_object("student_2", student_2))
print(describe_object("student_3", student_3))

<<<<<<< HEAD
=======

def some_func():
    return


some_int = 10
>>>>>>> f07bec3747a40695b27082ca48aae333e38da811
