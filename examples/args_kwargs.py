#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=WWm5DxTzLuk
Let's Learn Python #14 - *Args, **Kwargs

- arguments are declare within a function declaration
ARGS
- takes unlimited regular arguments
    - place in function argument to use
    - prevents program from crashing
'''

#################  ARGS  ######################
print('#################  ARGS  ######################')
def func(*args):
    for arg in args:
        print(arg)

func(1, 2, 3, 54, 'ham')

print('\n')

def func1(*args):
    for arg in args:
        print(arg)

list = [1, 2, 3, 54, 'ham']
func(list)
print('\n')
func(list[0], list[1], list[2])
print('\n')
print(*list)


#################  KWARGS  ######################
print('#################  KWARGS  ######################')
def func1(x = 234, y = 9):
    print(x, y)

func1()


def func1(x = 234, y = 9):
    print(x, y)

func1(x = 456, y = 3)


def func1(**kwargs): # cria um dicionário
    for item in kwargs.items():
        print(item)

func1(x = 456, y = 3)


def func1(**kwargs): # cria um dicionário
    for item in kwargs.values():
        print(item)

func1(x = 456, y = 3)


def func1(*args, **kwargs): # cria um dicionário
    for arg in args:
        print(arg)
    for item in kwargs.items():
        print(item)

func1(42,3.14, x = 456, y = 3)

