#!/usr/bin/python3
"""
    101-nqueens.py - Place N non-attacking queens on an N×N chessboard
    Calc N queens problem
    Args: n - number of queens on an NxN chessboard
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
n = sys.argv[1]
if "." in n or type(int(n)) is not int:
    print("N must be a number")
    exit(1)
if int(n) < 4:
    print("N must be at least 4")
    exit(1)
result = []
n = int(n)
for r in range(n):
    for c in range(n):
        continue  # result.append([r, c])
