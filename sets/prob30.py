## https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    c = str(input()).split()
    if c[0] == 'pop': s.pop()
    elif c[0] == 'remove': s.remove(int(c[1]))
    elif c[0] == 'discard': s.discard(int(c[1]))
print(sum(s))

# n = int(input())
# s = set(map(int, input().split())) 
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split()+['']))

# print(sum(s))