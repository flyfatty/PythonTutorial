# @Time : 2021/4/29 14:45
# @Author : LiuBin
# @File : decorator.py
# @Description : 
# @Software: PyCharm

"""python基础--装饰器
* python最难的概念之一
* 装饰器是修改其他函数的功能的函数
* 使用场景：日志（以该场景举例学习）、授权、DB连接等
>> 参考廖雪峰博客
"""

import functools


# 1. 编写一个简单的装饰器
def logit(a_func):
    @functools.wraps(a_func)  # functools.wraps 复制函数名称、注释文档、参数列表
    def decorated(*args, **kwargs):
        print("I am writing some log before executing a_func()")

        a_func(*args, **kwargs)

        print("I am writing some log after executing a_func()")

    return decorated


# 2. 使用装饰器语法装饰主函数
@logit
def a_function_requiring_decoration(name):
    print("I am {}".format(name))


a_function_requiring_decoration("FangJiayi")

print("\n*****************************************\n")


# 3. 带参数的装饰器 , 再包装一层函数即可
def logit(filename="123.log"):
    def log_decorator(a_func):
        @functools.wraps(a_func)
        def decorated(*args, **kwargs):
            print("I am writing some log to {} before executing a_func()".format(filename))
            a_func(*args, **kwargs)
            print("I am writing some log to {} after executing a_func()".format(filename))

        return decorated

    return log_decorator


@logit(filename="ABC.log")
def a_function_requiring_decoration(name):
    print("I am {}".format(name))


a_function_requiring_decoration("FangJiayi")

print("\n*****************************************\n")


# 4. 装饰器类，看起来更优雅，也有利于实现继承关系的功能，比如写日志的场景及既要写日志又要发邮件的场景。
class logit:
    def __init__(self, filename="123.log"):
        self.filename = filename

    def __call__(self, a_func, *args, **kwargs):
        @functools.wraps(a_func)
        def decorated(*args, **kwargs):
            a_func(*args, **kwargs)
            self.notify()

        return decorated

    def notify(self):
        print("I am writing some log to {} after executing a_func()".format(self.filename))


class email_logit(logit):
    def __init__(self, email, *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        print("I am writing some log to {} after executing a_func()".format(self.filename))
        print("I am sending a email to {} after executing a_func()".format(self.email))


@logit()
def a_function_requiring_decoration(name):
    print("I am {}".format(name))


a_function_requiring_decoration("FangJiayi")

print()


@email_logit(email="xxx@qq.com", filename="abc.log")
def a_function_requiring_decoration(name):
    print("I am {}".format(name))


a_function_requiring_decoration("FangJiayi")
