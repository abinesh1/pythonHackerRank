## https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
N = set(input().split())
m = int(input())
M = set(input().split())
print(len(N.intersection(M)))