class SchoolMember:
    """学校成员类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        '''Tell my details'''
        print('Name:{} Age:{}'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''表示老师的类'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{}'.format(self.salary))

class Student(SchoolMember):
    '''学生类'''
    def __init__(self, name, age, teacher):
        SchoolMember.__init__(self, name, age)
        self.teacher = teacher

    def tell(self):
        SchoolMember.tell(self)
        print('My teacher is:{}'.format(self.teacher.name))

t = Teacher('Mrs. Shrividya.', 40, 3000)
s = Student('Jml', 25, t)

print('*********')

menbers = [t, s]
for menber in menbers:
    menber.tell()
