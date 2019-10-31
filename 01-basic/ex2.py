#!/usr/bin/env python3
# # # # # # # # # # # #
# This file is used to show indent exception

def hello(name):
    if len(name)>0:
	print('Hello, ', name)
    else:
	print('May I know your name?')

hello('')
hello('user1')
