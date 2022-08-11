# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/8/11 12:42
Describe: 
"""


def binary_search(A, v, p=None, q=None):
    """
    二分查找

    :param A:
    :param v:
    :param p:
    :param q:
    :return:
    """
    if p is None:
        p = 0
    if q is None:
        q = len(A)
    mid = int((p + q) / 2)
    if v == A[mid]:
        return mid
    if p == q:
        return None
    if v > A[mid]:
        return binary_search(A, v, mid, q)
    else:
        return binary_search(A, v, p, mid)


if __name__ == '__main__':
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 8
    res = binary_search(X, x)
    print(res)
