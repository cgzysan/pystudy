#!/usr/bin/env python3
# by ysan

from core import logger
from lib.people import *
from conf import settings

user_data = {  # 初始化帐户数据
    'account_id': None,
    'is_authenticated': False,
    'account_data': None,
}

log_type = "system"  # 系统日志记录到文件中
system_logger = logger.logger(log_type)


def check_login(func):
    '''
    检查是否登录
    :return:
    '''
    def inner(*args, **kwargs):
        if user_data.get("is_authenticated", None):
            ret = func(*args, **kwargs)
            return ret
        else:
            # 登录流程：通过输入用户、密码，取用户得到用户对应的id的帐户，再对比密码
            print("\033[33;1mPlease sign in!\033[0m")
            person = Person()
            person.sign_in()
            if person.account:
                if person.account.authority == settings.AUTHORITY['student']:
                    person = Student(person.name, person.age, person.sex, person.account)
                elif person.account.authority == settings.AUTHORITY['teacher']:
                    pass
                user_data['is_authenticated'] = True
                user_data['account_id'] = person.account.account_id
                user_data['account_data'] = person
                print("\033[32;1mSign in success!\033[0m")
                system_logger.info("Account {} sign in successful!".format(user_data['account_id']))
            else:
                system_logger.info("Sign in failed")
    return inner


def check_authority(arg):
    '''检查权限'''
    def _check_authority(func):
        def inner(*args, **kwargs):
            person = user_data['account_data']
            if person.account.authority == arg:
                ret = func(*args, **kwargs)
                return ret
            else:
                print("Account \033[31;1m{}\033[0m permission access denied.".format(user_data['account_id']))
                system_logger.info("Account {} permission access denied.".format(user_data['account_id']))
        return inner
    return _check_authority


def enroll_student():
    '''学员注册'''
    student = Student()
    student.enroll()
    if student.account:
        print("Account [\033[31;1m%s\033[0m] register successful !" % student.account.account_id)
        system_logger.info("Account {} register successful".format(student.account.account_id))
        user_data['is_authenticated'] = True
        user_data['account_id'] = student.account.account_id
        user_data['account_data'] = student
        return student
    else:
        print("\033[31;1mAccount register failed !\033[0m")
        system_logger.info("Account register failed")
        return False


@check_login
@check_authority(settings.AUTHORITY['student'])
def select_course(base_db):
    if user_data['is_authenticated']:
        student = user_data['account_data']
        print("类型", type(student))
        if type(student.account.user_info) == dict and "courses" in student.account.user_info:
            print("You are learning a course,please check.【暂不支持已选课程情况】")  # 已有选课，不支持选课
            return

        # 列出学校课程详情
        print("课程信息".center(50, '-'))
        base_data = base_db.get_data()
        schools = base_data['schools']
        for school in schools:
            print("学校名称：\033[34;1m{}\033[0m".format(school.school_name))
            school.show_info('courses')
            print("--------------------------------------------------")

        # 选课
        flag = True
        while flag:
            print("Please input the course name of want to learn,"
                  "eg: [ \033[33;1mshanghai_an_school.java\033[0m ]")
            school_course = input(">>: ").strip()
            try:
                s_school = school_course.split(".")[0]
                s_course = school_course.split(".")[1]

                for school in schools:
                    if school.school_name == s_school:
                        for course in school.courses['courses']:
                            if course.name == s_course:
                                student.select_course(user_data['account_id'], s_course)    # 学员选课，用课名
                                school.add_attr_value('students')   # 学校添加学员
                                base_db.save_data(base_data)    # 保存数据到数据库
                                print("\033[32;1mSelect course success\033[0m")
                                system_logger.info("{} select course success".format(user_data['account_id']))
                                break   # 已匹配到课程，不需要再匹配
                        else:
                            print("\033[31;1mInput course error")   # 课程输入错误
                        break
                else:
                    print("\033[31;1mInput school error!\033[0m")  # 学校输入错误
                flag = False
            except Exception as e:
                print("\033[31;1mInput error!\033[0m")
                flag = True


@check_login
@check_authority(settings.AUTHORITY['student'])
def show_grade_info(base_db):
    attr_student = "students"
    attr_grade = "grades"
    school = which_school(base_db, user_data['account_id'], attr_student)   # 获取属于哪个学校
    class_name = user_data['account_data'].account.user_info.get('grade')
    if class_name:
        grades = getattr(school, attr_grade)[attr_grade]
        for grade in grades:
            if grade.name == class_name:
                grade.show_info()
                return True
        else:
            print("Your class \033[31;1m{}\033[0m no longer exists!".format(class_name))
            return False
    else:
        print("\033[31;1mYou did not join any class!\033[0m")
        return False


@check_login
def show_account_info():
    '''
    查看个人信息
    :return:
    '''
    print(" 个人信息 ".center(50, "-"))
    user_data['account_data'].account.show_info()


def modify_instance_info(person):
    '''
    修改输入的实例信息
    :param person:  实例
    :return:    修改后的实例
    '''
    flag = False
    list_dict = {'name': 'ygqygq2', 'sex': "male", 'age': 28}
    print("Input a dict type data to modify your info.eg: {}".format(list_dict))
    info = input(">>: ").strip()
    try:
        info_dict = eval(info)
    except Exception as e:
        info_dict = None
        print("\033[31;1mUser information input error!")

    if type(info_dict) == dict:
        for k in info_dict:  # 逐个修改属性
            setattr(person, k, info_dict[k])
        return person
    else:
        print("\033[31;1mInput is not dict type!\033[0m")


@check_login
def modify_info():
    '''
    修改学员信息
    :return:
    '''
    print(" 个人信息 ".center(50, "-"))
    user_data['account_data'].account.show_info()
    modify_instance_info(user_data['account_data'])
    user_data['account_data'].modify_info(user_data['account_id'])
    system_logger.info("Account {} modify account user info success".format(user_data['account_id']))


def which_school(base_db, account_id, role):
    '''
    根据account_id查询属于哪个学校
    :param base_db:     学校数据
    :param account_id:  用户id
    :param role:        查询属性值
    :return:    学校名称
    '''
    school_result = ""
    base_data = base_db.get_data()
    schools = base_data['schools']
    for school in schools:
        people_dict = getattr(school, role)
        people_list = people_dict[role]
        if people_list:
            for people in people_list:
                if people.account.account_id == int(account_id):
                    school_result = school
                    return school_result
    else:
        print("\033[31;1mDoes not belong to any schools!\033[0m")
    return school_result


def course_schedule(base_db):
    pass
