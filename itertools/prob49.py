## https://www.hackerrank.com/challenges/itertools-combinations/problem


from itertools import combinations
w, c = input().split()
for j in range(1, int(c)+1):
    print(*[''.join(i) for i in combinations(sorted(w), j)], sep = '\n')
