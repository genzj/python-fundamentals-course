# -*- encoding: utf-8 -*-


def add(a, b):
    print('enter function add, args: ', a, b)
    ans = a + b
    print('leave function add, return: ', ans)
    return ans


def sub(a, b):
    # duplicated code
    print('enter function sub, args: ', a, b)
    ans = a - b
    # duplicated code
    print('leave function sub, return: ', ans)
    return ans


print(add(1, 2))
print(sub(2, 1))
