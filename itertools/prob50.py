## https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement
w, n = input().split()
print(*[''.join(j) for j in combinations_with_replacement(sorted(w), int(n))], sep='\n')