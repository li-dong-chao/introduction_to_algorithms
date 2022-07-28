# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/7/28 13:07
Describe: 
"""


def insert_sort(x: list):
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and key < x[i]:
            x[i+1] = x[i]
            i -= 1
        x[i+1] = key


if __name__ == '__main__':
    a = [1, 4, 2, 5, 3, 9, 8, 7]
    insert_sort(a)
    print(a)
