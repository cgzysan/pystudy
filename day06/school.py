#!/usr/bin/env python3
# by ysan

'''
    http://www.murdermysterypa.com/thread-724-1-1.html
    先说结论：最有可能的人是管家木吉
    以下是我的分析：
    一开始看完，拥有最明显嫌疑的是助手比利，他报道了死者写作喜欢咬指甲的花边新闻，而且在秘书送茶去死者房间的时候抢过了茶壶，
    想自己去送，是有机会将氰化钾抹在茶壶上的，但是仔细想想就会发现至少在有一点是行不通的，死者只有在倒茶的时候才会用手接触
    茶壶的，但是茶杯却是干净的。
    所以，在茶壶上抹氰化钾是行不通的，那么就是通过其他的途径，仔细再看一遍会发现泡茶的过程中因为管家的原因发生了停电，这个
    时候在工作室赶稿子的死者肯定是等不了来电的，必然也就会去使用应急灯，可以猜测氰化钾就是抹在应急灯上，在死者使用了应急灯
    之后，使得氰化钾沾在了手上，后来死者咬了指甲，在一次去拿茶壶的时候感觉到身体的不对，从而中毒身亡。
    如果以上的犯罪手法成立，可以依次分析，这里主要分析管家：
    首先，在空闲时间进到死者工作室给应急灯抹上氰化钾，或者找个理由为别墅检查安全隐患，这些管家是可以做到的，
    其二，停电是管家造成的，这是一个案件发生的必然条件，
    其三，在最后进入死者房间的时候，管家带了手套，去关了亮着的应急灯，是可以顺便将上面的氰化钾擦干净的
    其四，管家关了应急灯之后，脱掉了手套，去感受死者体温，这里有处理占有氰化钾手套的嫌疑
    如果要石锤，找到管家的手套进行检测，如果一开始发现死者就报警，管家应该是还没有时间机会去处理手套
'''


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
