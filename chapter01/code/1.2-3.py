# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/7/28 12:50
Describe: 
"""
import math


def f(x):
    return 100*x**2 - 2**x


def main():
    n = 1
    while True:
        if f(n) < 0:
            print("解为: ", n)
            break
        n += 1


if __name__ == '__main__':
    main()
