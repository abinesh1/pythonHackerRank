## https://www.hackerrank.com/challenges/py-check-subset/problem

n = int(input())
for i in range(n):
    _ = int(input())
    s1 = set(map(int, input().split()))
    _ = int(input())
    s2 = set(map(int, input().split()))  
    print(True if len(s1.difference(s2)) == 0 else False)