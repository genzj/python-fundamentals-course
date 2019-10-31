# -*- encoding: utf-8 -*-


def printf(fmt, *args):
    print(fmt % args)


printf('hello %s', 'world')
printf('%d + %d = %d', 1, 2, 1 + 2)
