classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
#print(classmates[-4])
classmates.insert(1,'Jack')
classmates.pop(1)
#list can contain diferrent type of data
L = ['apple', 1, True]
print(L)
#list can contain other list
s = ['python', 'java', ['asp', 'php'],'scheme']
print(s)
#空list
L = []
print(len(L)) #0
