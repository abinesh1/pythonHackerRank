## https://www.hackerrank.com/challenges/py-the-captains-room/problem

k, rooms = input(), input().split()
single, multiple = set(), set()
for room in rooms:
    single.add(room) if room not in single else multiple.add(room)
print(*(single.difference(multiple)))