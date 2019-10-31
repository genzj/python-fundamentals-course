# -*- encoding: utf-8 -*-
def printinfo(arg1, arg2=10, *args, **kwargs):
    print("输出: ")
    print(arg1, arg2)
    for v in args:
        print(v)
    for key, val in kwargs.items():
        print("%s = %s" % (key, val))


print('call 1: ')
printinfo(5)
print('-' * 20)


print('call 2: ')
printinfo(*[1, 2, 3])
print('-' * 20)


print('call 3: ')
printinfo(*range(5))
print('-' * 20)


print('call 4: ')
printinfo(arg2=5, arg1=10)
print('-' * 20)


print('call 5: ')
printinfo(**{'arg1': 10, 'arg2': 100, 'argN': -1})
print('-' * 20)


print('call 6: ')
printinfo(1, 2, 3, *range(3), **{'argX': 10, 'argY': 100, 'argZ': -1})
