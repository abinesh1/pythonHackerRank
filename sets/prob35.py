## https://www.hackerrank.com/challenges/py-set-mutations/problem

_ = int(input())
s = set(map(int, input().split()))
for j in range(int(input())):
    x = input().split()
    s2 = set(map(int, input().split()))
    eval('s.{0}(s2)'.format(x[0]))
print(sum(s))