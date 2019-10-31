# -*- encoding: utf-8 -*-
def n():
    return 1, 2, 3


print(n())
# (1, 2, 3)

print(type(n()))
# <class 'tuple'>


print('-' * 20)


def swap(a, b):
    return b, a


a, b = 1, 2
a, b = swap(a, b)
print(a)  # 2
print(b)  # 1
