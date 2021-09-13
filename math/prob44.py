## https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath
n = complex(input())
print('{:f}'.format(abs(n)))
print('{:f}'.format(cmath.phase(n)))



# import cmath
# print(*cmath.polar(complex(input())), sep='\n')