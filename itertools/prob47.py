## https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
A, B = map(int, input().split()), map(int, input().split())
print(*product(A, B))