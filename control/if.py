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