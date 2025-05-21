import math
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end = ' ')
    print(repr(x*x*x).rjust(4))
    
print('{}网址： "{}!"'.format('菜鸟编程','www.runoob.com'))

print('常量PI的近似值为:{0:.3f}。'.format(math.pi))
print('常量PI的近似值为:{!r}。'.format(math.pi))
print('常量PI的近似值为:{!a}。'.format(math.pi))
print('常量PI的近似值为:{!s}。'.format(math.pi))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
