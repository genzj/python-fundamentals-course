# -*- encoding: utf-8 -*-

#########################
#   default argument
#########################


def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)


printinfo('runoob')  # age 为35
printinfo('runoob', 50)  # 指定age为50
print('-' * 20)


#########################
#   variable arguments
#########################


def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)


printinfo(10)
printinfo(70, 60, 50)
print('-' * 20)


#########################
#   keyword arguments
#########################


def printinfo(arg1, **vardict):
    print("输出: ")
    print(arg1)
    for key, val in vardict.items():
        print("%s = %s" % (key, val))


printinfo(10)
printinfo(70, a=60, b=50)
