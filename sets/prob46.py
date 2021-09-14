##  https://www.hackerrank.com/challenges/no-idea/problem

from collections import Counter
n, m = input().split()
N = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
c = Counter(N)
for i in c.keys():
    if i in A: happiness+= c[i]
    if i in B: happiness-= c[i]
print(happiness)


