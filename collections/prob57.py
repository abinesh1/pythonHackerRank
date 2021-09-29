##https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
d = deque()
for i in range(int(input())):
    text = input().split()
    arg = text[1:]
    cmd = str(text[0])+ '(' + str(','.join(arg)) + ')'
    eval("d.{0}".format(cmd))
print(*d)


