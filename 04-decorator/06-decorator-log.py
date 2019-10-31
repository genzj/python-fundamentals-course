# -*- encoding: utf-8 -*-
def log_it(f):
    def _wrapper(a, b):
        print('enter function %s, args: %s, %s ' % (f, a, b))
        ans = f(a, b)
        print('leave function %s, return: %s' % (f, ans))
        return ans

    return _wrapper


@log_it
def add(a, b):
    return a + b


@log_it
def sub(a, b):
    return a - b


print(add(1, 2))
print(sub(2, 1))
