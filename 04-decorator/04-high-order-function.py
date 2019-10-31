# -*- encoding: utf-8 -*-


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


def log_it(f):
    def new_f(a, b):
        return call_with_log(f, a, b)
    return new_f


add = log_it(_add)
sub = log_it(_sub)


print(add(1, 2))
print(sub(2, 1))
