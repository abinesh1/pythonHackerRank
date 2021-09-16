## https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict
A, B = map(int, input().split())
l1 = defaultdict(list)
for i in range(A):
    s = input()
    l1[s].append(i+1)
l2 = [input() for i in range(B)]
for x in l2:
    if x in l1.keys(): print(*l1[x])
    else: print('-1')