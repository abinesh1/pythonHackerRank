## https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product
n, m = map(int, input().split())
m1 = 0
lists = [list(map(int, input().split()))[1:] for i in range(n)]
combs = product(*lists)
for x in combs:
    s1 = sum(y**2 for y in x)
    if(s1%m>m1):
        m1 = s1%m
print(m1%m)

# optimum solution

# from itertools import product

# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for _ in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(max(results))


