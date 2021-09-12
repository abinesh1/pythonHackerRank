## https://www.hackerrank.com/challenges/py-check-strict-superset/problem

s1 = set(map(int, input().split()))
op = True
for i in range(int(input())):
    s2 = set(map(int, input().split()))
    if((len(s1) == len(s2)) or (len(s1.union(s2))>len(s1))):
        op = False
        break
print(op)

# A = set(input().split())

# for _ in range(int(input())):
#     if not A.issuperset(set(input().split())):
#         print(False)
#         break
# else:
#     print(True)