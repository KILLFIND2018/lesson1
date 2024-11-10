class Human:
    head = True
    def say_hello(self):
        print('Den')
#получаем доступ к human. Но Human не имеет доступ в stuent
class Student(Human):
    head = False
    def about(self):
        print('я студент')

class Teacher(Human):
    pass
# human = Human()
student = Student()
teacher = Teacher()
student.say_hello()
teacher.say_hello()
print(student.head)

