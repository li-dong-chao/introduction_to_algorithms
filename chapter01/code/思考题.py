# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/7/28 12:53
Describe: 
"""
from math import *

# t = 1000  # 1秒
# t = 1000*60  # 1分钟
# t = 1000*60*60  # 1小时
# t = 1000*60*60*24  # 1天
# t = 1000*60*60*24*30  # 1月
# t = 1000*60*60*24*365  # 1年
t = 1000*60*60*24*365*100  # 1世纪

n = 1
# n = 1052224334*10
while n * log(n, 2) < t:
    n += 1

print("log n解为", n - 1)

# for n!
n = 1
while factorial(n) < t:
    n += 1

print("n!解为:", n - 1)
