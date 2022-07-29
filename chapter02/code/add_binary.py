# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/7/29 13:33
Describe: 二进制和
"""


def add_binary(A: list, B: list):
    tmp = 0
    n = len(A)
    C = [0] * (n+1)
    l = list(range(n))
    l.reverse()
    for i in l:
        C[i+1] = (A[i] + B[i] + tmp) % 2
        tmp = 1 if A[i] + B[i] + tmp > 1 else 0
    C[i] = tmp
    return C


if __name__ == '__main__':
    A = [1, 0, 1, 1]
    B = [1, 1, 1, 1]
    C = add_binary(A, B)
    print(C)
