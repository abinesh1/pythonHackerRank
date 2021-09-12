## https://www.hackerrank.com/challenges/symmetric-difference/problem

m = input()
M = set(input().split())
n = input()
N = set(input().split())
diff = M.difference(N).union(N.difference(M))
print(*sorted(diff, key = int), sep='\n')