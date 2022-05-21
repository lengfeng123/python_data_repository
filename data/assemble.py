#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/5/21
# @file assemble.py

# 集合练习
# vowels = {'a', 'e', 'i', 'o', 'u', 'b', 'd'}
# # a = "abcd"
# # b = set(a)
# # print(b)
# # c = "hijk"
# # d = set(c)
# # print(d)
# # f = b.union(d)
# # k = d.union(b)
# # print(f)
# # print(k)
# # print(type(k))

x = {"a", "b", 1, 2}
y = {1, 3, 5}
z = x.difference(y)
print(z)

t = x.intersection(y)
print(t)
r = 2
y.add(r)
print(y)

y.discard(6)
print(y)

w = '{"name": "baby"}'
q = eval(w)
print(q)

tuple1 = (1, 2)
tuple2 = ("name",)
print(type(tuple1))
print(type(tuple2))
print(tuple1)
print(tuple2)

gg = ["name", "sex", "score"]
hh = ["里斯", "男", 150]
dd = dict(zip(gg, hh))
print(dd)
