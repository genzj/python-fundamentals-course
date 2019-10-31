# -*- encoding: utf-8 -*-


# function must be renamed
def _add(a, b):
    ans = a + b
    return ans


def _sub(a, b):
    ans = a - b
    return ans


def call_with_log(f, a, b):
    print('enter function %s, args: %s, %s' % (f, a, b))
    ans = f(a, b)
    print('leave function %s, return %s' % (f, ans))
    return ans


def add(a, b):
    return call_with_log(_add, a, b)


# almost duplicated with add(a, b)
def sub(a, b):
    return call_with_log(_sub, a, b)


print(add(1, 2))
print(sub(2, 1))
