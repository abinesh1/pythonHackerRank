## https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
w = input().split()
for x in sorted(permutations(w[0], int(w[1]))):
    print(*x, sep = '')


# s,n = input().split()
# print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')    