# _*_ coding: utf-8 _*_
import math
#函数名是指向一个函数对象的引用
# a = abs
# print(a(-1))

# n1 = 255
# print(hex(n1))

#函数没有返回值时，返回None，return None可以写成return
#函数什么也不做，空函数。
# def nop():
#     pass


#函数返回多个值,其实就是一个tuple



def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = move(100, 100, 60, math.pi / 6)
print(r)


