#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author ZhangSir
# @date 2022/5/19
# @file list1.py

# a = ["name", "ma"]
# c = ''.join(a)
#
# android = "oppo and vivo"
# phone = list(android)
# print(phone)
# for i in phone:
#     print(i)


dict = {
    "name": "张三",
    "sex": "女"
}

p = dict["name"]
print(p)

dict["score"] = 80
print(dict)
print("==============")

# for i in dict:
#     print(i)
#     print(dict[i])

# for i in sorted(dict):
#     print(i,dict[i])

lista = []
for k, v in sorted(dict.items()):
    lista.append(v)
print(lista)

# if '张三' not in dict:
#     print("错错啦")
# else:
#     print("错误")

