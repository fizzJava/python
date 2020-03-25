# -*- coding: utf-8 -*-
classmates = ('Michael', 'Bob','Tracy')
print(classmates)
t = (1, 2)
print(t)
t = ()
print(t)
#这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = (1)
print(t)
t = (1,)
print(t)
#"可变的"tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'C'
t[2][1] = 'D'
print(t)    