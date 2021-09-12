## https://www.hackerrank.com/challenges/py-set-difference-operation/problem

_, N = int(input()), set(input().split())
_, M = int(input()), set(input().split())
print(len(N.difference(M)))