#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0 or n is None:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    p = []
    for i in range(n):
        p.append([])
        p[i].append(1)

        for j in range(1, i):
            p[i].append(p[i - 1][j - 1] + p[i - 1][j])
        if(n != 0):
            p[i].append(1)

    p[0] = [1]

    return p
