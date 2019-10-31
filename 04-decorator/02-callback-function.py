# -*- encoding: utf-8 -*-


def add(a, b):
    ans = a + b
    return ans


def sub(a, b):
    ans = a - b
    return ans


def call_with_log(f, a, b):
    print('enter function %s, args: %s, %s' % (f, a, b))
    ans = f(a, b)
    print('leave function %s, return %s' % (f, ans))
    return ans


# all caller must be modified
print(call_with_log(add, 1, 2))
print(call_with_log(sub, 2, 1))
