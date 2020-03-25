# _*_ coding: utf-8 _*_
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中没有
#重复的key
#要创建一个set需要一个list作为输入集合
s = set([1, 2, 3])
print(s)

#重复的元素在set中自动被过滤
s = set([1, 2, 3, 3, 4,])
print(s)
#使用add(key)可以向set中添加元素，可以重复添加，但不会有效果
s.add(4)
print(s)
#使用remove(key)删除元素,删除一个不存在的key会报错。
#s.remove(5)

#set可以看做数学意义上无序和无重复元素的集合
a = set([1, 2, 3])
b = set([4, 5, 6])
print(a & b)
print(a | b)

#tuple虽然是不可变对象，但是把它放到set或dic中，会发生什么呢?
t = (1, 2, 3)
dic = {t:11}
print(dic)
t = (1, 2, [4, 5])#出错
#dic = {t:11} 

t = (1, 2, 3)
s = set([])
s.add(t)
print(s)
s.add(5)
print(s)
t = ([1,2]) #出错
s.add(t)