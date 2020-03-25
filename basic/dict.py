# _*_ coding: utf-8 _*_
d = {'Michael':95, 'Bob':75, 'Tracy':65}
print(d['Michael'])
d['Adam'] = 100
print(d)
#print(d['Jack']) 报错

#判断key是否存在的方法
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))
print(d.get('Michael', 100))

#删除一个key，可以使用pop(key)方法，对应的value也会从dic中删除。
#删除一个不存在的key会报错。只要访问一个不存在的key，事先都要做判断。
print(d)
d.pop('Bob')
print(d)
if 'William' in d:
    d.pop('William')

#dict的key必须是一个不可变对象
