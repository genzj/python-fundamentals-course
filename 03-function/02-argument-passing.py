# -*- encoding: utf-8 -*-


def change_me(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


mylist = [10, 20, 30]
change_me(mylist)
print("函数外取值: ", mylist)
