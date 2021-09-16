## https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import permutations
n = input()
l = input().split()
prob= 0
m = int(input())
for x in permutations(l, m):
    if('a' in x):
        prob+=1
print(prob/len(list(permutations(l, m))))


# from itertools import combinations

# N = int(input())
# L = input().split()
# K = int(input())

# C = list(combinations(L, K))
# F = filter(lambda c: 'a' in c, C)
# print("{0:.3}".format(len(list(F))/len(C)))