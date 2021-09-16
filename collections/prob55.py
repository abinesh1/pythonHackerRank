## https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
n = int(input())
shoes = map(int, input().split())
Count = Counter(shoes)
sale = 0
for i in range(int(input())):
    size, value = input().split()
    if(Count[int(size)]>0):
        sale+= int(value)
        Count[int(size)]-=1
print(sale)