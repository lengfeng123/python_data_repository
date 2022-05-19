#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/5/18
# @file list.py


import random

uu = []

wait_time = random.randint(1, 60)
print(wait_time)

prices = []
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
# 一个对象在另一个对象中吗？用in检查
for i in word:
    if i in vowels:
        print(i)

found = []
found.append('a')
found.append('b')
found.append('c')

print(found)

if 'u' in found:
    print('u')
else:
    print("没有找到这个对象")

if 'm' not in found:
    found.append('m')
    print(found)

for i in found:
    print(i)

for i in range(1, 5):
    print(i)

for i in range(5):
    print(i)

found.remove("m")
print(found)

a = found.pop()
print(a)
print(type(a))
print(found)

n = found.pop(0)
print(n)
print(found)
