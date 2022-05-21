#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/5/21
# @file function.py

# 0,值是None,空串，空的内置数据结构，值为False
a = bool(-1)
print(a)


# return 可以返回一个值，也可以返回一个数据结构
def test_all(data1, data2):
    ab = list()
    ab.append(data1)
    ab.append(data2)
    return ab


qq = test_all(data2=3, data1=5)
print(qq)
