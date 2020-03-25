#函数参数有正常定义的必选参数，还可以使用默认参数、可变参数和关键字参数，使得
#函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

#计算x^2的代码
def power(x):
    return x * x
#计算x^5的代码
def power_2(x, n):
    ret = 1
    while n > 0:
        ret *= x
        n -= 1
    return ret
print(power_2(2,5))

#必选参数在前，默认参数在后。
#默认参数降低了函数的调用难度
#默认参数有个大坑
def add_end(L = []):
    L.append('End')
    return L
print(add_end([1, 2, 3]))
print(add_end())#['End']
print(add_end())#['End', 'End']
print(add_end())#['End', 'End', 'End']
#出现上述情况是因为：
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#定义默认参数要牢记一点：默认参数必须指向不变对象！

#如何修改上面的例子
def add_end2(L = None):
    if L is None:
        L = []
    L.append('End')
    return L
print(add_end2())
print(add_end2())   

#可变参数 计算 a^2 + b^2 + c^2 + ...
#在不使用可变参数的情况下，需要使用list或者tuple
def calc(nums):
    ret = 0
    for n in nums:
        ret += n*n
    return ret
print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))
#使用可变参数
def calc_2(*nums):
    ret = 0
    for n in nums:
        ret += n*n
    return ret

print(calc_2(1, 2))
print(calc_2())
#如果已经有个list或者tuple，但是要调用一个可变参数，应该怎么办？ 
l = [1, 2 ,3]
t = (1, 2, 3)
print(calc_2(l[0], l[1], l[2]))
print(calc_2(t[0], t[1], t[2]))
#上面的方法表示有点tiresome
print(calc_2(*l))
print(calc_2(*t))

#关键字参数
#可变参数允许你传入0个或者任意个参数，这些可变参数在函数调用时自动组装成一个tuple。
#而关键字参数允许你传入0个或者任意个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict.
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30,)
person('Michael', 30, city = 'Beijing', gender = 'M', job = 'Engineer')

#非组装的调用方法
extra = {'city': 'Beijing', 'gender': 'M', 'job': 'Engineer'}
person('Michael', 30, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数
#对于关键字参数，我们是可以传入任一不受限制的参数，至于到底传了哪些，就要在函数内部，通过kw检查
def  person_2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    if 'gender' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

#如果要限制关键字参数的名字，就要使用命名关键字参数，例如，只接受city和job作为关键字参数
def person_3(name, age, *, city, job): # * 在这里作为分隔符  
    print(name, age, city, job)

#调用方式如下
person_3('Jack', 24, city = 'Beijing', job = 'Engineer')

#可变参数和命名关键字同时使用时，就不需要 * 分割符了
def person_4(name, age, *args, city, job):
    print(name, age, args, city, job)
person_4('Jack', 24, 1, 2, 3, 4, city = 'Beijing', job = 'Engineer')

#命名关键字可以有缺省值，从而简化调用
def person_5(name, age, *, city = 'Beijing', job):
    print(name, age, city, job)

#由于命名关键字city有缺省值，调用时，可不传入city参数
person_5('Jack', 24, job = 'Engineer')

#参数组合
#必选参数 默认参数 可变参数 关键字参数 命名关键字参数，这5种参数可以组合使用。但是注意
#5种参数的定义顺序必须是：必选参数 默认参数 可变参数 命名关键字参数 关键字参数






    