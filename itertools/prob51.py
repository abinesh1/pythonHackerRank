## https://www.hackerrank.com/challenges/compress-the-string/problem


from itertools import groupby
n = input()
print(*[(len(list(y)), int(x)) for x,y in groupby(n)], sep = ' ')