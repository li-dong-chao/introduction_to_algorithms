# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/8/4 12:25
Describe: 归并排序
"""


def merge(A, p, q, r):
    """
    合并操作

    :param A: 数组
    :param p: 左端点
    :param q: 中间点
    :param r: 右端点
    :return:
    """
    n1 = q - p + 1
    n2 = r - q
    L = [0.0] * n1
    R = [0.0] * n2
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
    L.append(float("inf"))
    R.append(float("inf"))
    i, j = 0, 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A


def merge_sort(A, p=None, r=None):
    """
    归并排序

    :param A: 待排序的数组
    :param p: 左端点
    :param r: 右端点
    :return:
    """
    if p is None:
        p = 0
    if r is None:
        r = len(A)-1
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A


if __name__ == '__main__':
    a = [1, 4, 2, 5, 3, 9, 8, 7]
    # a = [2, 1]
    merge_sort(a)
    print(a)
