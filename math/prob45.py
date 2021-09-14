## https://www.hackerrank.com/challenges/find-angle/problem

import math
x, y = int(input()), int(input())
print(str(int(round(math.degrees(math.atan2(x,y)))))+chr(176))