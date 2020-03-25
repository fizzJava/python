# -*- coding: utf-8 -*-f
age = 18
if age >= 18:
    print('your age is:', age)
    print('adult')
else: 
    print('your age is:', age)
    print('teenager')
#elif 细化条件判断
if age >= 18:
    print('your age is:', age)
    print('adult')
elif age >= 6:
    print('your age is:', age)
    print('teenager')
else:
    print('your age is:', age)
    print('kid')
#if判断条件的简写 
x = ()
if x:
    print('True')

#input的返回数据类型是str.对于用户的输入如何检查并捕获程序运行时的错误。
birth = input('your birth:')
if int(birth) < 2000:
    print('00前')
else:
    print('00后')
