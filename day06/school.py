#!/usr/bin/env python3
# by ysan


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self, stu_obj):
        print("为学员%s办理手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, tea_obj):
        print("雇佣新员工%s" % tea_obj.name)
        self.teachers.append(tea_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print("Teacher [%s] is teaching course [%s]" % (self.name, self.course))

    def tell(self):
        print('''
        ------ info of teacher %s ------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, sid, grade):
        super(Student, self).__init__(name, age, sex)
        self.name = name
        self.age = age
        self.sid = sid
        self.grade = grade

    def tell(self):
        print('''
        ------ info of student %s ------
        Name:%s
        Age:%s
        Sex:%s
        Sid:%s
        Grade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.sid, self.grade))

    def pay_tuition(self, amount):
        print("%s has paid tuition for %s" % (self.name, amount))


school = School("玉溪", "郴州")
t1 = Teacher('An', 35, 'F', 15000, 'linux')
t2 = Teacher('Y', 32, 'M', 16000, 'python')
t1.tell()
t2.tell()
s1 = Student('Z', 20, 'M', 5000, 'C++')
s2 = Student('J', 22, 'F', 6000, 'Go')
s1.tell()
s2.tell()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)
