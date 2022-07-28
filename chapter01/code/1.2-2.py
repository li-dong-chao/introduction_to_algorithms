# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/7/28 12:40
Describe: 
"""

import math


def f(x):
    return x - 8*math.log2(x)


def main():
    solution = []
    n = 1
    while True:
        if f(n) < 0:
            if len(solution) == 0:
                solution.append(n)
                print("左端点为: ", n)
            else:
                pass
        elif f(n) >= 0 and len(solution) == 1:
            print("右端点为: ", n-1)
            break
        n += 1


if __name__ == '__main__':
    main()
