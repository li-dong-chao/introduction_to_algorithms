# -*- encoding: utf-8 -*-

"""
Author: LittleTom
DateTime: 2022/8/2 12:23
Describe: 选择排序
"""


def choice_sort(A):
    """
    选择排序

    :param A: 要排序的数组
    :return:
    """
    for i in range(len(A)-1):
        tmp = i
        for j in range(i+1, len(A)):
            if A[j] < A[tmp]:
                tmp = j
        A[i], A[tmp] = A[tmp], A[i]
    return A


if __name__ == '__main__':
    a = [1, 4, 2, 5, 3, 9, 8, 7]
    choice_sort(a)
    print(a)
