# _*_ coding: utf-8 _*_

#尾递归，主要看解释器会不会给你做优化
def fact(n):
    return factor_item(n, 1)

def factor_item(num, product):
    if num == 1:
        return product
    return factor_item(num - 1, num * product)

print(fact(5))

