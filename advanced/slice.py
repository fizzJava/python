# _*_ coding: utf-8 _*_ 

#取一个list或者tuple的部分元素是非常常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#根据下标
#use loop
#取list得前三个元素
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

#slice用于取指定索引范围的操作
print(L[0:3])
#支持倒数切片
print(L[-2:]) #取后面的两个的元素

#关于slice的一些操作
L = list(range(100))
#取前10个数
print(L[:10])
#取后10个数
print(L[-10:])
#取11-20个数
print(L[10:20])
#取前10个数，每两个取一个
print(L[:10:2])
#取所有数，每5个取一个
print(L[::5])
#什么都不写，就可以复制一个list
print(L[:])


#tuple也是一种list, 唯一区别是tuple不可变。因此tuple也可适用于切片操作，只不过结果
#仍然是tuple
print((0, 1, 2, 3, 4, 5)[:3])

#字符串也可以看成是一种list
print('abc中国人'[:4])
#在很多编程语言中，都有针对字符串的截取函数，例如PHP中的substring,但是在python中，没有字符串
#截取函数，都是通过切片（slice）来完成的。