# -*- encoding: utf-8 -*-
from functools import wraps


def log_it(level='DEBUG'):
    def _log_it(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):
            print('[%s] enter function %s, args: %s, kwargs %s ' % (level, f.__name__, args, kwargs))
            ans = f(*args, **kwargs)
            print('[%s] leave function %s, return: %s' % (level, f.__name__, ans))
            return ans
        return _wrapper
    if callable(level):
        # shortcut with default parameters
        return log_it()(level)
    return _log_it


@log_it(level='WARN')
def add(a, b):
    return a + b


@log_it
def mul(a, b):
    return a * b


print(add(1, 2))
print(mul(1, 2))
